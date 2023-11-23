from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class AuthCodeViewSet(viewsets.ModelViewSet):
    queryset = AuthCode.objects.all()
    serializer_class = AuthCodeSerializer


class DeviceTokenViewSet(viewsets.ModelViewSet):
    queryset = DeviceToken.objects.all()
    serializer_class = DeviceTokenSerializer
