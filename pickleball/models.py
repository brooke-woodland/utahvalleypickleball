from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Location(models.Model):
    court_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, default='UT')
    courts = models.IntegerField(default=0)
    openTime = models.TimeField(default= None)
    closeTime = models.TimeField(default= None)
    indoor = models.BooleanField(default=False)
        

