from django.db import models
from .validators import validate_min_one


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField("Departure Date")
    return_date = models.DateField("Return Date")
    number_of_travelers = models.IntegerField(validators=[validate_min_one])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination