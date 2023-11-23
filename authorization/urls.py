from django.urls import path, include
from rest_framework import routers

from authorization.views import *


router = routers.SimpleRouter()
router.register(r'tokens', TokenViewSet)
router.register(r'authcode', AuthCodeViewSet)
router.register(r'device_tokens', DeviceTokenViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
