import string
import random

from rest_framework import serializers

from .models import *


class AuthCodeSerializer(serializers.ModelSerializer):
    # user: int = serializers.IntegerField()
    # token: str = serializers.CharField()

    # add_date: str = serializers.DateTimeField()
    # expiration_date: str = serializers.DateTimeField()
    # code: str = serializers.CharField(max_length=10)
    # is_used: str = serializers.BooleanField()

    class Meta:
        model = AuthCode
        fields = ["user", "add_date", "expiration_date", "code", "is_used"]


class DeviceTokenSerializer(serializers.ModelSerializer):
    device: int = serializers.IntegerField()
    token: str = serializers.CharField(max_length=32)