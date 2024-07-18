from django.utils import timezone
from django.shortcuts import render
from .models import Event


def upcoming_events(request):
    today = timezone.now().date()
    upcoming_list = Event.objects.filter(date__gt=today)
    return render(request, "events/upcoming_events.html", {"upcoming": upcoming_list})
