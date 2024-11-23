from xmlrpc.client import MAXINT

from django.db import models

# Create your models here.
class pokemon(models.Model):
    id = models.IntegerField(MAXINT = 153)
    name= models.CharField()
    cries = models.CharField()
    height = models.CharField()
    weight = models.IntegerField()
    location = models.CharField()
    image = models.CharField()

class abilities(models.Model):
    ability_name = models.CharField()
    ability_url = models.CharField()
    hidden = models.BooleanField()
    slot = models.IntegerField()

