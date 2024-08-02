from django.urls import path
from .views import create_trip_view

app_name = 'bookings'
urlpatterns = [
    path("trips/new/", create_trip_view, name="create_trip"),
]