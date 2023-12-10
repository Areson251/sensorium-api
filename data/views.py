from base64 import b64decode
import numpy as np

from authorization.backends import DeviceTokenAuthentication

from django.forms.models import model_to_dict
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.settings import BASE_DIR
from data.serializers import CreatePhotoSerializer

from .sensor_reading import SensorReading
from control.models import IndicatorValues
from control.serializers import (
    IndicatorIdSerializer,
    IndicatorValuesSerializer,
)


@extend_schema(
    parameters=[CreatePhotoSerializer],
    responses={400: CreatePhotoSerializer.errors, 200: None},
    description="Сохранение картинок вида base64 локально в папку media и показания датчика в таблицу indicator-values.",
)
@api_view(["POST"])
# @authentication_classes([DeviceTokenAuthentication])
@permission_classes([IsAuthenticated])
def save_photo(request):
    user = request.user
    data = request.data

    serializer = CreatePhotoSerializer(data=data)
    if not serializer.is_valid():
        return Response({"error": "Invalid data"}, status=400)

    indicator_id = serializer.data.get("indicator_id")
    image_path = serializer.data.get("image_path") + serializer.data.get("filename") 
    content = b64decode(serializer.data.get("image"))

    # path = BASE_DIR / "media" / serializer.data.get("filename")
    # with open(path, "wb") as file:
    #     file.write(content)

    sensor_tool = SensorReading()
    detected_value = sensor_tool.get_results(content)

    if not detected_value:
        return Response({"error": "didn't found any gague plate"}, status=404)
    
    indicator_value = IndicatorValues.objects.create(
    indicator_id=indicator_id,
    value=detected_value,
    image_path=image_path,)

    indicator_value_serialized = model_to_dict(indicator_value)
    return Response(indicator_value_serialized, status=200)
