from django.db import models
from datetime import date
import datetime

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    location=models.CharField(max_length=50)
    fromdate = models.DateField()
    fromtime =models.TimeField()
    todate = models.DateField()
    totime =models.TimeField()
    enddate = models.DateField()
    endtime =models.TimeField()
    host_email = models.EmailField()
    host_pass = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    def is_past_due(self):
        return ( date.today() < self.enddate)

class Participant(models.Model):
    name=models.CharField(max_length=20)
    phone =models.CharField(max_length=20) 
    email=models.EmailField()
    participation_type=models.CharField(max_length=10)
    no_of_people=models.IntegerField()
    event_id=models.IntegerField()

    def __str__(self):
        return self.name


    
