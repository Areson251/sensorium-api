from rest_framework import serializers


class CreatePhotoSerializer(serializers.Serializer):
    image: str = serializers.CharField()
    filename: str = serializers.CharField()
