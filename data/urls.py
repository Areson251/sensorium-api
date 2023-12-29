from django.urls import path

from data import views

urlpatterns = [
    path("save_photo/", views.save_photo, name="save-photo"),
]
