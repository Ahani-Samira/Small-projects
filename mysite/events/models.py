from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField("Event date")
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name
