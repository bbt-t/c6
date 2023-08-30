from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import MailingViewSet, ClientsViewSet

route = DefaultRouter()
route.register("mailing_schedule", MailingViewSet)
route.register("clients", ClientsViewSet)

urlpatterns = [
    *route.urls,
    path(
        "api-token-auth/", obtain_auth_token, name="api_token_auth"
    ),  # Маршрут для получения токена
]
