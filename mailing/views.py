from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q

from .forms import CreateMessageForm, CreateClientForm, EmailScheduleForm
from .mixins import AddCreatorMixin, CreatorOrManagerFilterMixin, AddFromCreatorMixin
from .models import Client, EmailSchedule, Message, MailingLog


class ClientListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    login_url = "/auth/login/"

    model = Client
    context_object_name = "clients"


class EmailScheduleListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    login_url = "/auth/login/"

    model = EmailSchedule
    context_object_name = "schedule_objects"


class MessageListView(CreatorOrManagerFilterMixin, LoginRequiredMixin, ListView):
    login_url = "/auth/login/"

    model = Message
    context_object_name = "email_schedule_messages"


class MailingLogListView(LoginRequiredMixin, ListView):
    login_url = "/auth/login/"

    model = MailingLog
    context_object_name = "log_schedule_messages"

    def get_queryset(self):
        q = super().get_queryset()
        if self.request.user.is_manager:
            return q
        return q.filter(Q(settings__creator=self.request.user))


class ClientCreateView(AddCreatorMixin, LoginRequiredMixin, View):
    login_url = "/auth/login/"

    template_name = "mailing/message_form.html"
    form_class = CreateClientForm


class MessageCreateView(AddCreatorMixin, LoginRequiredMixin, View):
    login_url = "/auth/login/"

    template_name = "mailing/message_form.html"
    form_class = CreateMessageForm


class EmailScheduleCreateView(AddFromCreatorMixin, LoginRequiredMixin, CreateView):
    login_url = "/auth/login/"

    model = EmailSchedule
    form_class = EmailScheduleForm
    success_url = reverse_lazy("mailing_list")


class EmailScheduleUpdateView(AddFromCreatorMixin, LoginRequiredMixin, UpdateView):
    login_url = "/auth/login/"

    model = EmailSchedule
    form_class = EmailScheduleForm
    success_url = reverse_lazy("mailing_list")
