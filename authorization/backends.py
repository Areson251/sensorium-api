from rest_framework import authentication, exceptions

from .models import DeviceTokens


class DeviceTokenAuthentication(authentication.BaseAuthentication):
    """
    Permission check for authorized devices.
    """

    def authenticate(self, request):
        payload = request.headers.get("Authorization")
        if payload is None:
            return (None, None)
        token_type, token = payload.split(" ")

        if token_type != 'DeviceToken':
            return (None, None)

        try:
            device = DeviceTokens.objects.get(token=token).device
        except DeviceTokens.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such device")

        return (device.user, None)
