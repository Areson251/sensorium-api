from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    user_id: str = serializers.IntegerField()
    token: str = serializers.CharField()


class AuthCodeSerializer(serializers.Serializer):
    user_id: str = serializers.IntegerField()
    token: str = serializers.CharField()

    user_id: str = serializers.IntegerField()
    add_date: str = serializers.DateTimeField()
    expiration_date: str = serializers.DateTimeField()
    code: str = serializers.CharField(max_length=10)
    is_used: str = serializers.BooleanField()


class DeviceTokenSerializer(serializers.Serializer):
    device_id: str = serializers.IntegerField()
    token: str = serializers.CharField(max_length=32)