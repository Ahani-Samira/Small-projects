from django.core.exceptions import ValidationError
import datetime


def validate_min_one(value):
    if value < 1:
        raise ValidationError("The number of travelers  cannot be less than one person!")


def validate_not_past_date(value):
    if value < datetime.date.today():
        raise ValidationError("The date cannot be in the past. Only today and future dates are allowed.")


def validate_time_does_not_go_back(first_date, second_date):
    if first_date > second_date:
        raise ValidationError("You can't travel back in time :)")
