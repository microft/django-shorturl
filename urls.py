from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^shorturl/', include('shorturl.foo.urls')),

    (r'^(?P<longurl>http://.+)$', 'shorturl.shorturlapp.views.shorten'),
    (r'^(?P<longurl>https://.+)$', 'shorturl.shorturlapp.views.shorten'),
    (r'^(?P<longurl>ftp://.+)$', 'shorturl.shorturlapp.views.shorten'),
    (r'^(?P<code>[a-z\d]+)/$', 'shorturl.shorturlapp.views.unshorten'),
    (r'^(?P<code>[a-z\d]+)/stats/$', 'shorturl.shorturlapp.views.stats'),
    (r'^(?P<code>[a-z\d]+)/info/$', 'shorturl.shorturlapp.views.info'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
