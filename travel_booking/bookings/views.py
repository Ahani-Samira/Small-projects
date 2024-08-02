from django.shortcuts import render
from .forms import TripForm
from .models import Trip

def create_trip_view(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TripForm()
    return render(request,"bookings/create_trip.html", {"form": form})


def list_trips_view(request):
    form = TripForm(request.GET)
    trips = Trip.objects.all()
    return render(request, "bookings/list_trips.html", {"form":form, "trips":trips})
