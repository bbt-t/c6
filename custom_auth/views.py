from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import TemplateView

from .forms import UserRegForm


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


@method_decorator(unauthenticated_user, name="dispatch")
class RegisterView(View):
    template_name = "registration/register.html"

    def get(self, request, *args, **kwargs):
        user_form = UserRegForm()
        return render(request, self.template_name, {"user_form": user_form})

    def post(self, request, *args, **kwargs):
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password2"])
            new_user.is_activ = False
            new_user.save()

            if self._send_email_verify(
                request, new_user, user_form.cleaned_data.get("email")
            ):
                messages.success(
                    request, "Подтверди свою почту чтобы активировать аккаунт"
                )

        return render(request, self.template_name, {"user_form": user_form})

    @staticmethod
    def _send_email_verify(request, user, to_email) -> bool:
        mail_subject = "Подтверди почту"
        message = render_to_string(
            "custom_auth/template_activate_account.html",
            {
                "domain": get_current_site(request).domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
                "protocol": "https" if request.is_secure() else "http",
            },
        )

        email = EmailMessage(
            mail_subject, message, to=[to_email], from_email=settings.EMAIL_FROM
        )
        return email.send()


@method_decorator(unauthenticated_user, name="dispatch")
class EmailActivate(View):
    @staticmethod
    def _get_user(uidb64):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=urlsafe_base64_decode(uidb64).decode())
        except (
            TypeError,
            ValueError,
            OverflowError,
            ValidationError,
            user_model.DoesNotExist,
        ) as e:
            print(e)

    def get(self, request, uidb64, token):
        user = self._get_user(uidb64)
        if user and default_token_generator.check_token(user, token):
            user.is_active, user.is_verified = True, True
            user.save()
            login(request, user)
            return redirect("homepage")

        return redirect("invalid_email_verify", uidb64)


@method_decorator(unauthenticated_user, name="dispatch")
class InvalidEmailVerify(TemplateView):
    template_name = "custom_auth/invalid_verify.html"


# https://docs.djangoproject.com/en/4.1/topics/auth/default/#all-authentication-views
# Django также содержит следующие ниже представления, позволяющие
# пользователям сбрасывать свой пароль:
# •• PasswordResetView: позволяет пользователям сбрасывать свой пароль.
# Генерирует одноразовую ссылку с токеном и отправляет ее на электронный ящик пользователя;
# •• PasswordResetDoneView: сообщает пользователям, что им было отправлено электронное
# письмо, содержащее ссылку на сброс пароля;
# •• PasswordResetConfirmView: позволяет пользователям устанавливать новый пароль;
# •• PasswordResetCompleteView: представление страницы об успехе, на которую
# пользователь перенаправляется после успешного сброса пароля.
