from rest_framework import serializers


class CreatePhotoSerializer(serializers.Serializer):
    indicator_id: int = serializers.IntegerField()
    image_path: str = serializers.CharField()
    image: str = serializers.CharField()
    filename: str = serializers.CharField()
