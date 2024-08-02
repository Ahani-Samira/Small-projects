from django.urls import path
from .views import create_trip_view, list_trips_view, update_trip_view

app_name = 'bookings'
urlpatterns = [
    path("trips/new/", create_trip_view, name="create_trip"),
    path("trips/", list_trips_view, name="list_trips"),
    path("trips/<int:pk>/edit/", update_trip_view, name="update_trip"),
]