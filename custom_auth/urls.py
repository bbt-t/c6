from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from .views import RegisterView, InvalidEmailVerify, EmailActivate

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("verify_email/<uidb64>/<token>/", EmailActivate.as_view(), name="activate"),
    path(
        "invalid_email_verify/<uidb64>",
        InvalidEmailVerify.as_view(),
        name="invalid_email_verify",
    ),
    path(
        "invalid_email_verify/",
        RedirectView.as_view(url="/"),
        name="invalid_email_redirect",
    ),
]
