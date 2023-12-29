from django.urls import path

from authorization import views

urlpatterns = [
    path("generate-device-code/", views.generate_device_password, name="generate-device-code"),
    path("set-device-token/", views.set_device_token, name="set-device-token"),
]
