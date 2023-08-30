from django.forms import ModelForm, DateTimeInput, ValidationError
from django.utils import timezone

from .models import Message, Client, EmailSchedule


class CreateMessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ("creator",)


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ("creator",)


class EmailScheduleForm(ModelForm):
    class Meta:
        model = EmailSchedule
        exclude = "creator", "status"
        widgets = {"send_time": DateTimeInput(attrs={"type": "datetime-local"})}

    def clean_send_time(self):
        send_time = self.cleaned_data.get("send_time")
        if send_time and send_time < timezone.now():
            raise ValidationError("Выберите дату и время, которые позже текущей.")
        return send_time
