from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Location(models.Model):
    court_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(default='UT')
    courts = models.IntegerField(default=0)
    OpenTime = models.TimeField(default=0)
    CloseTime = models.TimeField(default=0)
    Indoor = models.BooleanField
        

