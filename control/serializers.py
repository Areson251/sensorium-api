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
    name: str = serializers.CharField(max_length=100)
    description: str = serializers.CharField()

    class Meta:
        model = Equipment
        fields = ["user_id", "name", "description", "add_date", "update_date"]


class IndicatorsSerializer(serializers.ModelSerializer):
    equipment_id: int = serializers.IntegerField()
    # indicator_type: str = serializers.CharField(max_length=100)
    min_value: str = serializers.CharField(max_length=100)
    max_value: str = serializers.CharField(max_length=100)

    class Meta:
        model = Indicators
        fields = [
            "equipment_id",
            "indicator_type",
            "min_value",
            "max_value",
            "add_date",
            "update_date",
        ]


class IndicatorValuesSerializer(serializers.ModelSerializer):
    indicator_id: int = serializers.IntegerField()
    value: str = serializers.CharField(max_length=100)
    image_path: str = serializers.CharField(max_length=100)

    class Meta:
        model = IndicatorValues
        fields = ["indicator_id", "value", "add_date", "image_path"]


class EquipmentIdSerializer(serializers.Serializer):
    equipment_id: int = serializers.IntegerField()

class IndicatorIdSerializer(serializers.Serializer):
    indicator_id: int = serializers.IntegerField()
