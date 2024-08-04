from django.shortcuts import render, get_object_or_404, redirect
from .forms import TripForm
from .models import Trip
from rest_framework import viewsets
from .serializers import TripSerializer


def create_trip_view(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookings:list_trips")
    else:
        form = TripForm()
    return render(request,"bookings/create_trip.html", {"form": form})


def list_trips_view(request):
    form = TripForm(request.GET)
    trips = Trip.objects.all()
    return render(request, "bookings/list_trips.html", {"form":form, "trips":trips})


def update_trip_view(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect("bookings:list_trips")
    else:
        form = TripForm(instance=trip)
    return render(request, "bookings/update_trip.html", {"form":form})


def delete_trip_view(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect("bookings:list_trips")
    return render(request, "bookings/confirm_delete.html", {"trip": trip})


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
