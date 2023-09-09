from base64 import b64encode
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def checks_is_member_of_manager_group(user) -> bool:
    """
    Checks if the user is a manager or not
    :param user: User model
    :return: is or not
    """
    # также и на is_manager можно проверять
    return user.groups.filter(name="my_group").exists()


def generate_number_image(number) -> str:
    """
    Create number image.
    :param number: num for create
    :return: bytes in string
    """
    image = Image.new("RGB", (200, 100), "white")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("static/fonts/blue_stone.ttf", 48)

    text_position = (50, 30)
    draw.text(text_position, str(number), font=font, fill="black")

    image_bytes = BytesIO()
    image.save(image_bytes, format="PNG")

    return b64encode(image_bytes.getvalue()).decode("utf-8")
