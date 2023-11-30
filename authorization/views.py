import string
import random

from base64 import b64decode

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


from .serializers import *
from .models import *

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_device_password(request):
    data = request.data

    token = request.headers["Authorization"].split(" ")[1]
    user = Token.objects.get(key=token).user_id
    password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))

    data["user"] = user
    data["code"] = password
    data["is_used"] = False

    serializer = AuthCodeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"code": serializer.data["code"]}, status=201)
    return Response(serializer.errors, status=400)

@api_view(["POST"])
def set_auth_code(request): 
    serializer = AuthCodeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    return Response(status=200)

@api_view(["POST"])
def set_device_token(request):
    password = request.data["code"]
    
    serializer = DeviceTokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    return Response(status=200)
