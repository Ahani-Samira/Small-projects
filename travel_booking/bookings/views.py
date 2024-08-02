from django.shortcuts import render
from .forms import TripForm


def create_trip_view(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TripForm()
    return render(request,"bookings/create_trip.html", {"form": form})

