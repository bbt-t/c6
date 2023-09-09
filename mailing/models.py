from django.db import models
from custom_auth.models import CustomUser


class Client(models.Model):
    """
    Service Client.
    """

    email = models.EmailField(unique=True, verbose_name="почта клиента")
    full_name = models.CharField(max_length=128, verbose_name="имя клиента")
    comment = models.CharField(
        max_length=512, blank=True, null=True, verbose_name="комментарий"
    )

    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="кто создал запись"
    )

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"

        indexes = [
            models.Index(fields=["email"]),
        ]


class Message(models.Model):
    """
    Message to send.
    """

    subject = models.CharField(max_length=128, verbose_name="тема письма")
    body = models.CharField(max_length=1024, verbose_name="тест письма")

    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="кто создал запись"
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    # def save(self, *args, **kwargs):
    #     if not self.pk:  # If the object is being created
    #         self.creator = get_user(request=request)
    #     super().save(*args, **kwargs)


class EmailSchedule(models.Model):
    """
    Sending emails (settings).
    """

    INTERVAL_CHOICES = [
        ("daily", "раз в день"),
        ("weekly", "раз в неделю"),
        ("monthly", "раз в месяц"),
    ]

    STATUS_CHOICES = [
        ("running", "запущена"),
        ("disabled", "отключена"),
    ]

    send_time = models.DateTimeField(verbose_name="дата и время начала рассылки")
    interval = models.CharField(
        max_length=7, choices=INTERVAL_CHOICES, verbose_name="интервал"
    )
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default="disabled", verbose_name="статус"
    )
    clients = models.ManyToManyField(Client, verbose_name="для клиентов")
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, verbose_name="сообщение для рассылки"
    )

    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="кто создал запись"
    )

    class Meta:
        verbose_name = "настройка рассылки"
        verbose_name_plural = "настройки рассылок"

    def __str__(self) -> str:
        return f"send_time: {self.send_time.date()}, interval: {self.interval}, message: {self.message.subject}"

    def get_interval_display_ru(self) -> str:
        """
        get interval in Russian.
        """
        return dict(self.INTERVAL_CHOICES).get(self.interval, "Неизвестно")

    def get_status_display_ru(self) -> str:
        """
        get status in Russian.
        """
        return dict(self.STATUS_CHOICES).get(self.status, "Неизвестно")


class MailingLog(models.Model):
    """
    Logs.
    """

    STATUS_CHOICES = [
        ("success", "успешно"),
        ("failure", "ошибка"),
    ]

    attempt_time = models.DateTimeField(
        auto_now_add=True, verbose_name="дата в время попытки"
    )
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, verbose_name="статус"
    )
    response = models.TextField(blank=True, null=True, verbose_name="ответ")
    settings = models.ForeignKey(
        EmailSchedule, on_delete=models.CASCADE, verbose_name="настройка рассылки"
    )

    class Meta:
        verbose_name = "результат рассылки"
        verbose_name_plural = "результат рассылок"

    def __str__(self) -> str:
        return f"attempt_time: {self.attempt_time.date()}, status: {self.status}"

    def get_interval_status_ru(self) -> str:
        """
        get status in Russian.
        """
        return dict(self.STATUS_CHOICES).get(self.status, "Неизвестно")
