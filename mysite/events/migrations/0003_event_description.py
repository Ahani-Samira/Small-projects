# Generated by Django 5.0.6 on 2024-07-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_data_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
