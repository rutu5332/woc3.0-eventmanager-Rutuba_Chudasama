from django.db import models
from datetime import date

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    location=models.CharField(max_length=50)
    fromdate = models.DateField()
    fromtime =models.CharField(max_length=10)
    todate = models.DateField()
    totime =models.CharField(max_length=10)
    enddate = models.DateField()
    endtime =models.CharField(max_length=10)
    host_email = models.EmailField()
    host_pass = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    def is_past_due(self):
        return date.today() < self.enddate

class Participant(models.Model):
    name=models.CharField(max_length=20)
    phone =models.CharField(max_length=20) 
    email=models.EmailField()
    rtype=models.CharField(max_length=10)
    participants=models.IntegerField()
    event=models.IntegerField()

    def __str__(self):
        return self.name


    
