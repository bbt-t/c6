from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs) -> None:
        """
        If is_verified = false then is_manager cannot be set to True.
        """
        if not self.is_verified and self.is_manager:
            raise ValueError("Cannot set is_manager to True if is_verified is False")
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]
