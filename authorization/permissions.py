from rest_framework import authentication, exceptions

from .models import DeviceTokens


class IsDeviceAuthenticated(authentication.BaseAuthentication):
    """
    Permission check for authorized devices.
    """

    def authenticate(self, request):
        token = request.META.get("HTTP_X_USERNAME")
        if not token:
            return None

        try:
            device = DeviceTokens.objects.get(token=token)
        except DeviceTokens.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such device")

        return (device, None)
