from django.core.management import BaseCommand

from custom_auth.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(
            email="admin@admin.com",
            first_name="Ad",
            last_name="Min",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("123")
        user.save()
