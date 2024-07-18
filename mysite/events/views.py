from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from .models import Event


def upcoming_events(request):
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    upcoming_list = Event.objects.filter(date__gt=last_week)
    return render(request, "events/upcoming_events.html", {"upcoming": upcoming_list})
