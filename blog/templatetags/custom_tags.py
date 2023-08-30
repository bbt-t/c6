from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def media_path(image_name) -> str:
    """
    Replaces with the default image.
    :return: image address
    """
    no_img_pic_name = "blog_images/no_image.webp"
    if not image_name:
        return f"{settings.MEDIA_URL}{no_img_pic_name}"

    return f"{settings.MEDIA_URL}{image_name}"


@register.simple_tag
def full_name(user) -> str:
    """
    Replaces with the full name or default.
    :return:
    """
    if user:
        if user.first_name and user.last_name:
            return f"{user.first_name} {user.last_name}"

    return "Анонимный пользователь"
