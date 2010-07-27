from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from models import ShortUrl

BASE = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def toBaseN(num, base):
  new_num_string=''
  current=num
  n = len(base)
  while current!=0:
    remainder = current%n
    remainder_string=base[remainder]
    new_num_string=remainder_string+new_num_string
    current=current/n
  return new_num_string

def fromBaseN(num,base):
  indexes = range(len(num))
  new_number = 0
  for i in indexes:
    value = base.index(num[i])
    x = value*pow(len(base),indexes[::-1][i])
    new_number = new_number + x
  return new_number

def shorten(request, longurl):
  t = ShortUrl.objects.get_or_create( longurl=longurl )
  response = 'http://%s/%s' % (request.META['HTTP_HOST'], toBaseN(t[0].id,BASE))
  return HttpResponse(response)

def unshorten(request, code):
  code = fromBaseN(code,BASE)
  l = ShortUrl.objects.filter(id=code)
  if not l:
    return HttpResponseNotFound()
  if len(l)==1:
    l[0].clicks = l[0].clicks + 1
    l[0].save()
    return HttpResponseRedirect( l[0].longurl)
  else:
    return HttpResponse('Acho que nao conheco esse short url!')

def stats(request,code):
  code = fromBaseN(code,BASE)
  l = ShortUrl.objects.filter(id=code)
  return HttpResponse(l[0].clicks)

def info(request,code):
  return HttpResponse(repr(request))
  code = fromBaseN(code,BASE)
  l = ShortUrl.objects.filter(id=code)
  return HttpResponse(l[0].longurl)
