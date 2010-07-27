from django.db import models

class ShortUrl(models.Model):
  longurl = models.CharField(max_length=500)
  clicks = models.IntegerField()
  clicks.default = 0

  def __unicode__(self):
    return self.longurl
        


# Create your models here.
