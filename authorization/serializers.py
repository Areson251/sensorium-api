from rest_framework import serializers


class AuthCodeSerializer(serializers.ModelSerializer):
    user: int = serializers.IntegerField()
    token: str = serializers.CharField()

    add_date: str = serializers.DateTimeField()
    expiration_date: str = serializers.DateTimeField()
    code: str = serializers.CharField(max_length=10)
    is_used: str = serializers.BooleanField()


class DeviceTokenSerializer(serializers.ModelSerializer):
    device: int = serializers.IntegerField()
    token: str = serializers.CharField(max_length=32)