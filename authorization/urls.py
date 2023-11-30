from django.urls import path
from authorization import views 

urlpatterns = [
    path("generate_device_code/", views.generate_device_password, name="device-password"),
    path("set_device_token/", views.set_device_token, name="device-token"),
]
