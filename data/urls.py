from django.urls import path

from data import views

urlpatterns = [
    path("photos/", views.save_photo, name="save-photo"),
]
