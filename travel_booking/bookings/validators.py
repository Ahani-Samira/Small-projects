from django.core.exceptions import ValidationError


def validate_min_one(value):
    if value < 1:
        raise ValidationError("The number of travelers  cannot be less than one person!")