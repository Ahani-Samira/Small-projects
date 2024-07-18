from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("upcoming/", views.upcoming_events, name="upcoming_events"),
    ]