from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        queryset = Devices.objects.filter(user=user)
        serializer = DevicesSerializer(queryset, many=True)
        return Response(serializer.data)


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticated,)


class IndicatorsViewSet(viewsets.ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer
    permission_classes = (IsAuthenticated,)


class IndicatorValuesViewSet(viewsets.ModelViewSet):
    queryset = IndicatorValues.objects.all()
    serializer_class = IndicatorValuesSerializer
    permission_classes = (IsAuthenticated,)
