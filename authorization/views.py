from base64 import b64decode

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import *


@api_view(["POST"])
def set_auth_code(request): 
    serializer = AuthCodeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    return Response(status=200)

@api_view(["POST"])
def set_device_token(request):
    serializer = DeviceTokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    return Response(status=200)
