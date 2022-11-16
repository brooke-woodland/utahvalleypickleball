from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Location(models.Model):
    court_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    courts = models.IntegerField(default=0)
    OpenTime = models.TimeField(default=0)
    CloseTime = models.TimeField(default=0)
    Indoor = models.BooleanField

    def save(self):
       self.state = self.state.upper()
       self.state = self.state.slice(1)

       if self.state != 'UT':
        raise ValidationError('Error: Address is not in Utah')
       else:
        self.state = self.state
        

