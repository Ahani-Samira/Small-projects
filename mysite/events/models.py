from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    data = models.DateTimeField("Event date")
    location = models.CharField(max_length=250)
    
