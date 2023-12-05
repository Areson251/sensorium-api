from django.urls import path
from authorization import views 

urlpatterns = [
    path("generate_device_code/", views.generate_device_password, name="dgenerate-device-code"),
    path("set_device_token/", views.set_device_token, name="set-device-token"),
]
