from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate, m2m_changed
from django.dispatch import receiver

from custom_auth.models import CustomUser


def block_user(user_id) -> None:
    """
    Логика блокировки пользователей:
    В вашем представлении (view) или в сервисной логике вы можете реализовать
    функциональность блокировки пользователей, используя методы вашей переопределенной модели пользователя.
    :param user_id: users id
    """
    user = CustomUser.objects.get(id=user_id)
    user.is_active = False
    user.save()


def create_manager_group_and_permissions(_, **kwargs) -> None:
    """
    Create new group.
    """
    manager_group, created = Group.objects.get_or_create(name="manager")
    view_customuser_permission = Permission.objects.get(codename="view_customuser")
    view_emailschedule = Permission.objects.get(codename="view_emailschedule")
    delete_emailschedule = Permission.objects.get(codename="delete_emailschedule")

    content_type = ContentType.objects.get_for_model(CustomUser)
    block_customuser_permission, created = Permission.objects.get_or_create(
        codename="block_customuser",
        name="Can block custom users",
        content_type=content_type,
    )

    manager_group.permissions.add(
        view_emailschedule,
        delete_emailschedule,
        view_customuser_permission,
        block_customuser_permission,
    )


@receiver(post_migrate)
def create_group_and_permissions(sender, **kwargs) -> None:
    """
    Create signal.
    """
    if sender.name == "custom_auth":
        create_manager_group_and_permissions(sender, **kwargs)


@receiver(m2m_changed, sender=Group.user_set.through)
def update_user_field(sender, instance, action, reverse, model, pk_set, **kwargs):
    """
    Create signal.

    При добавлении в группу пользователя изменяем поле is_manager = True
    """
    print("update_user_field")
    if action == "post_add" and model == CustomUser and instance.name == "manager":
        print("update_user_field_into_if")

        for user_id in pk_set:
            user = CustomUser.objects.get(pk=user_id)
            user.is_manager = True
            user.save()
