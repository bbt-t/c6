from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path("", include("blog.urls")),
    path("auth/", include("custom_auth.urls")),
    path("service/", include("mailing.urls")),
    path("api/", include("api.urls")),
]
