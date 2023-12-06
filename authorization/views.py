import random
import string
from base64 import b64decode

from django.db.models import F
from django.shortcuts import render
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .permissions import *
from .serializers import *


@extend_schema(
    parameters=[AuthCodeSerializer],
    responses={400: ErrorsSerializer, 200: AuthCodeSerializer},
    description="Генерация пароля для регистрации девайса пользователя.",
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_device_password(request):
    user = request.user
    code = "".join(
        random.choices(
            string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10
        )
    )
    auth_code = AuthCodes.objects.create(code=code, user=user)
    return Response({"code": auth_code.code}, status=200)


@extend_schema(
    responses={400: status.HTTP_418_IM_A_TEAPOT, 200: None},
    description="Регистрация девайса пользователя.",
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def set_device_token(request):
    serializer = AuthCodeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    user = request.user
    code = request.data["code"]
    auth_code = AuthCodes.objects.filter(
        code=code, is_used=False, expiration_date__gte=timezone.now()
    ).first()

    if not auth_code:
        return Response(
            {"error": "code is invalid"}, status=status.HTTP_418_IM_A_TEAPOT
        )

    auth_code.is_used = True
    auth_code.save()

    device = Devices.objects.create(user=user)
    device_token = DeviceTokens.objects.create()

    device_token.device_id = device.id
    device_token.save()

    return Response({"device_token": device_token.token}, status=200)


# @api_view(["POST"])
# def set_auth_code(request):
#     serializer = AuthCodeSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(serializer.errors, status=400)
#     return Response(status=200)
