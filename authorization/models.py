from django.db import models
from django.contrib.auth.models import User

from control.models import Devices


class AuthCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    add_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10)
    is_used = models.BooleanField()

    class Meta:
        db_table = "authcode"


class DeviceToken(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.SET_NULL, null=True)
    token = models.CharField(max_length=32)

    class Meta:
        db_table = "devicetoken"