from django.urls import path, include
from rest_framework import routers

from control.views import *


router = routers.SimpleRouter()
router.register(r'devices', DevicesViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'indicators', IndicatorsViewSet)
router.register(r'indicator_values', IndicatorValuesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
