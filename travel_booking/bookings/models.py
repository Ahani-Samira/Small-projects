from django.db import models
from .validators import validate_min_one, validate_not_past_date, validate_time_does_not_go_back
from django.utils import timezone


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField("Departure Date", default=timezone.now(), validators=[validate_not_past_date])
    return_date = models.DateField("Return Date")
    number_of_travelers = models.IntegerField(validators=[validate_min_one])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination

    def clean(self):
        super().clean()
        if self.return_date and self.departure_date:
            validate_time_does_not_go_back(self.departure_date, self.return_date)
