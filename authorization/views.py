import string
import random

from base64 import b64decode

from django.utils import timezone
from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import *
from .serializers import *
from .models import *


@extend_schema(
    parameters=[AuthCodeSerializer],
    responses={400: AuthCodeSerializer.errors, 200: None},
    description="Генерация пароля для регистрации девайса пользователя.",
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_device_password(request):
    user = request.user
    code = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))
    auth_code = AuthCodes.objects.create(code=code, user=user)
    return Response({"code": auth_code.code}, status=200)

@extend_schema(
    parameters=[AuthCodeSerializer],
    responses={400: AuthCodeSerializer.errors, 200: None},
    description="Регистрация девайса пользователя.",
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def set_device_token(request): 
    user = request.user
    code = request.data["code"]
    auth_code = AuthCodes.objects.filter(code=code).first()

    if timezone.now() > auth_code.expiration_date: 
        return Response({"error": "code waiting time has expired"}, status=status.HTTP_418_IM_A_TEAPOT)
    if auth_code.is_used: 
        return Response({"error": "code was already used"}, status=status.HTTP_418_IM_A_TEAPOT)

    auth_code.is_used = True
    auth_code.save()

    device_token = DeviceTokens.objects.create()
    device = Devices.objects.create(user=user)
    device_token.device_id = device.id
    device_token.save()

    return Response({"device_token": device_token.token}, status=200) 

# @api_view(["POST"])
# def set_auth_code(request): 
#     serializer = AuthCodeSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(serializer.errors, status=400)
#     return Response(status=200)