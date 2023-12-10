from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Devices, Equipment, Indicators, IndicatorValues
from .serializers import (
    DevicesSerializer,
    EquipmentIdSerializer,
    EquipmentSerializer,
    IndicatorIdSerializer,
    IndicatorsSerializer,
    IndicatorValuesSerializer,
)


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

    def list(self, request):
        user = request.user
        queryset = Equipment.objects.filter(user=user)
        serializer = EquipmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        data = request.data

        serializer = EquipmentSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        queryset = Equipment.objects.filter(user=user, name=data["name"])
        if queryset.exists():
            return Response(
                {"error": "This name is already used"},
                status=status.HTTP_418_IM_A_TEAPOT,
            )

        equipment = Equipment.objects.create(
            user=user, name=data["name"], description=data["description"]
        )
        equipment_serialized = model_to_dict(equipment)
        return Response(equipment_serialized, status=200)

    def update(self, request, pk=None):
        user = request.user
        data = request.data

        serializer = EquipmentSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        equipment = Equipment.objects.filter(user=user, pk=pk)
        if not equipment.exists():
            return Response({"error": "not found"}, status=404)

        equipment = equipment.first()
        equipment.name = data["name"]
        equipment.description = data["description"]
        equipment.save()
        equipment_serialized = model_to_dict(equipment)
        return Response(equipment_serialized, status=200)

    def destroy(self, request, pk=None):
        user = request.user
        equipment = Equipment.objects.filter(user=user, pk=pk)
        if not equipment.exists():
            return Response({"error": "not found"}, status=404)
        equipment.delete()
        return Response(status=200)


class IndicatorsViewSet(viewsets.ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        data = request.data
        serializer = EquipmentIdSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        equipment_id = request.data["equipment_id"]
        if not self.valid_equipment_id(user, equipment_id):
            return Response(
                {"error": "no equipment with such id"},
                status=404,
            )

        queryset = Indicators.objects.filter(equipment_id=equipment_id)
        serializer = IndicatorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        data = request.data

        serializer = IndicatorsSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        equipment_id = request.data["equipment_id"]
        if not self.valid_equipment_id(user, equipment_id):
            return Response(
                {"error": "no equipment with such id"},
                status=404,
            )

        indicator = Indicators.objects.create(
            equipment_id=equipment_id,
            min_value=data["min_value"],
            max_value=data["max_value"],
        )
        indicator_serialized = model_to_dict(indicator)
        return Response(indicator_serialized, status=200)

    def update(self, request, pk=None):
        user = request.user
        data = request.data

        serializer = IndicatorsSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        equipment_id = request.data["equipment_id"]
        if not self.valid_equipment_id(user, equipment_id):
            return Response(
                {"error": "no equipment with such id"},
                status=404,
            )

        indicator = Indicators.objects.filter(pk=pk)
        if not indicator.exists():
            return Response({"error": "not found"}, status=404)

        indicator = indicator.first()
        indicator.min_value = data["min_value"]
        indicator.max_value = data["max_value"]
        indicator.save()
        indicator_serialized = model_to_dict(indicator)
        return Response(indicator_serialized, status=200)

    def destroy(self, request, pk=None):
        user = request.user
        data = request.data
        serializer = EquipmentIdSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        equipment_id = request.data["equipment_id"]
        if not self.valid_equipment_id(user, equipment_id):
            return Response(
                {"error": "no equipment with such id"},
                status=404,
            )

        indicator = Indicators.objects.filter(pk=pk)
        if not indicator.exists():
            return Response({"error": "not found"}, status=404)
        indicator.delete()
        return Response(status=200)

    def valid_equipment_id(self, user, equipment_id):
        queryset = Equipment.objects.filter(user=user, id=equipment_id)
        return queryset.exists()


class IndicatorValuesViewSet(viewsets.ModelViewSet):
    queryset = IndicatorValues.objects.all()
    serializer_class = IndicatorValuesSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        data = request.data
        serializer = IndicatorIdSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        indicator_id = request.data["indicator_id"]
        if not self.valid_indicator_id(user, indicator_id):
            return Response(
                {"error": "no indicator with such id"},
                status=404,
            )

        queryset = IndicatorValues.objects.filter(indicator_id=indicator_id)
        serializer = IndicatorValuesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        data = request.data

        serializer = IndicatorValuesSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        indicator_id = request.data["indicator_id"]
        if not self.valid_indicator_id(user, indicator_id):
            return Response(
                {"error": "no indicator with such id"},
                status=404,
            )

        indicator_value = IndicatorValues.objects.create(
            indicator_id=indicator_id,
            value=data["value"],
            image_path=data["image_path"],
        )
        indicator_value_serialized = model_to_dict(indicator_value)
        return Response(indicator_value_serialized, status=200)

    def update(self, request, pk=None):
        user = request.user
        data = request.data

        serializer = IndicatorValuesSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        indicator_id = request.data["indicator_id"]
        if not self.valid_indicator_id(user, indicator_id):
            return Response(
                {"error": "no indicator with such id"},
                status=404,
            )

        indicator_value = IndicatorValues.objects.filter(pk=pk)
        if not indicator_value.exists():
            return Response({"error": "not found"}, status=404)

        indicator_value = indicator_value.first()
        indicator_value.value = data["value"]
        indicator_value.image_path = data["image_path"]
        indicator_value.save()
        indicator_value_serialized = model_to_dict(indicator_value)
        return Response(indicator_value_serialized, status=200)

    def destroy(self, request, pk=None):
        user = request.user
        data = request.data
        serializer = IndicatorIdSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        indicator_id = request.data["indicator_id"]
        if not self.valid_indicator_id(user, indicator_id):
            return Response(
                {"error": "no indicator with such id"},
                status=404,
            )

        indicator_value = IndicatorValues.objects.filter(pk=pk)
        if not indicator_value.exists():
            return Response({"error": "not found"}, status=404) 
        indicator_value.delete()
        return Response(status=200)

    def valid_indicator_id(self, user, indicator_id):
        equipment_id = Indicators.objects.filter(id=indicator_id).first().id
        queryset = Equipment.objects.filter(user=user, id=equipment_id)
        return queryset.exists()
