from rest_framework import permissions

from .models import AuthCodes


class IsDeviceAuthenticated(permissions.BasePermission):
    """
    Permission check for authorized devices.
    """

    def has_permission(self, request, view):
        code = request.data["code"]
        auth_code = AuthCodes.objects.filter(code=code).exists()
        return auth_code 