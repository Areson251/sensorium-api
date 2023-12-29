from rest_framework import serializers

from .models import *


class AuthCodeSerializer(serializers.ModelSerializer):
    code: str = serializers.CharField(min_length=10, max_length=10)

    class Meta:
        model = AuthCodes
        fields = ["code"]


class DeviceTokenSerializer(serializers.ModelSerializer):
    device: int = serializers.IntegerField()
    token: str = serializers.CharField(max_length=40)

    class Meta:
        model = DeviceTokens
        fields = ["token"]


class ErrorsSerializer(serializers.Serializer):
    code: bool = serializers.BooleanField()
    message: str = serializers.CharField()
