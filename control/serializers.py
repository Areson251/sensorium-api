from rest_framework import serializers

# ModelSerializer, 
class DevicesSerializer(serializers.Serializer):
    user: int = serializers.IntegerField()  # Посмотреть Serializer Relationships

    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()


class EquipmentSerializer(serializers.Serializer):
    user_id: str = serializers.IntegerField()

    name: str = serializers.CharField(max_length=100)
    description: str = serializers.CharField()
    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()


class IndicatorsSerializer(serializers.Serializer):
    equipment: str = serializers.IntegerField()
    equipment_type: str = serializers.CharField(max_length=100)
    min_value: str = serializers.CharField(max_length=100)
    max_value: str = serializers.CharField(max_length=100)
    add_date: str = serializers.DateTimeField()
    update_date: str = serializers.DateTimeField()


class IndicatorValuesSerializer(serializers.Serializer):
    device_id: str = serializers.IntegerField()
    indicator: str = serializers.IntegerField()
    value: str = serializers.CharField(max_length=100)
    add_date : str = serializers.DateTimeField()
    image_path: str = serializers.CharField(max_length=100)