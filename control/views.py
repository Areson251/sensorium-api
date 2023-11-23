from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class IndicatorsViewSet(viewsets.ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer


class IndicatorValuesViewSet(viewsets.ModelViewSet):
    queryset = IndicatorValues.objects.all()
    serializer_class = IndicatorValuesSerializer
