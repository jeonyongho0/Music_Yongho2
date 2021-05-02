from django.db import models

from django.utils import timezone
import datetime




class Music(models.Model):
    music_name = models.CharField(max_length=50)
    music_brand = models.CharField(max_length=100)
    music_price = models.IntegerField(default=0)
    music_buy = models.DatatimeField()
    music_producer = models.CharField(max_length=50)
    music_quantity = models.PositiveInteger()
