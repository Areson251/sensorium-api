from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    # data
    path("api/v1/data/", include("data.urls")),

    # control
    path("api/v1/control/", include("control.urls")),


    # user authorization
    path("api/v1/auth/", include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    
    path("api/v1/authorization/", include("authorization.urls")),

    # swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
