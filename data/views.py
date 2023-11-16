from base64 import b64decode

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.settings import BASE_DIR
from data.serializers import CreatePhotoSerializer


@extend_schema(
    parameters=[CreatePhotoSerializer],
    responses={400: CreatePhotoSerializer.errors, 200: None},
    description="Сохранение картинок вида base64 локально в папку media.",
)
@api_view(["POST"])
def save_photo(request):
    serializer = CreatePhotoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    path = BASE_DIR / "media" / serializer.data.get("filename")

    content = b64decode(serializer.data.get("image"))
    with open(path, "wb") as file:
        file.write(content)

    return Response(status=200)
