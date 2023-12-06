from rest_framework import serializers

from .models import *


class DevicesSerializer(serializers.ModelSerializer):
    user_id: int = serializers.IntegerField()
    name: str = serializers.CharField(max_length=100)
    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()

    class Meta:
        model = Devices
        fields = ["user_id", "name", "add_date", "update_date"]


class EquipmentSerializer(serializers.ModelSerializer):
    user_id: int = serializers.IntegerField()

    name: str = serializers.CharField(max_length=100)
    description: str = serializers.CharField()
    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()


class IndicatorsSerializer(serializers.ModelSerializer):
    equipment_id: int = serializers.IntegerField()
    equipment_type: str = serializers.CharField(max_length=100)
    min_value: str = serializers.CharField(max_length=100)
    max_value: str = serializers.CharField(max_length=100)
    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()


class IndicatorValuesSerializer(serializers.ModelSerializer):
    device_id: int = serializers.IntegerField()
    indicator: str = serializers.IntegerField()
    value: str = serializers.CharField(max_length=100)
    add_date: str = serializers.DateTimeField()
    image_path: str = serializers.CharField(max_length=100)
