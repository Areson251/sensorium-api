from datetime import datetime, timedelta
import os
import binascii

from django.db import models
from django.contrib.auth.models import User

from control.models import Devices


class AuthCodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    add_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=datetime.utcnow() + timedelta(days=1))
    code = models.CharField(max_length=10)
    is_used = models.BooleanField(default=False)

    class Meta:
        db_table = "auth_codes"


class DeviceTokens(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.SET_NULL, null=True)
    token = models.CharField(max_length=40)

    class Meta:
        db_table = "device_tokens"

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_token(cls):
        return binascii.hexlify(os.urandom(20)).decode()