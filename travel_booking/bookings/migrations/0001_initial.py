# Generated by Django 5.0.6 on 2024-07-19 16:42

import bookings.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('departure_date', models.DateField(verbose_name='Departure Date')),
                ('return_date', models.DateField(verbose_name='Return Date')),
                ('number_of_travelers', models.IntegerField(validators=[bookings.validators.validate_min_one])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
