from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Event


def upcoming_events(request):
    now= timezone.now()
    last_week = now.date() - timedelta(days=7)
    upcoming_list = Event.objects.filter(date__gt=last_week)
    return render(request, "events/upcoming_events.html", {"upcoming": upcoming_list, "now": now})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/detail.html", {"event": event})