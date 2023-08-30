from django.apps import AppConfig


class CustomAuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "custom_auth"
    verbose_name = "AUTH"

    def ready(self):
        import custom_auth.signals
