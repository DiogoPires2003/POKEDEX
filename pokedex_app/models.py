from xmlrpc.client import MAXINT

from django.db import models


# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    cries = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.IntegerField()
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


class Abilities(models.Model):
    ability_name = models.CharField(max_length=255)
    ability_url = models.CharField(max_length=255)
    hidden = models.BooleanField(default=False)
    slot = models.IntegerField()

