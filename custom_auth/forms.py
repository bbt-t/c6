from django import forms
from django.contrib.auth.forms import UserCreationForm

from custom_auth.models import CustomUser


class UserRegForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            "unique": "Пользователь с такой почтой уже существует.",
        },
    )

    class Meta:
        model = CustomUser
        fields = "email", "password1", "password2"
