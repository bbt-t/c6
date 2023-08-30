from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q

from .forms import CreateMessageForm, CreateClientForm, EmailScheduleForm
from .mixins import AddCreatorMixin, CreatorOrManagerFilterMixin, AddFromCreatorMixin
from .models import Client, EmailSchedule, Message, MailingLog


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class ClientListView(CreatorOrManagerFilterMixin, ListView):
    model = Client
    context_object_name = "clients"


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class EmailScheduleListView(CreatorOrManagerFilterMixin, ListView):
    model = EmailSchedule
    context_object_name = "schedule_objects"


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class MessageListView(CreatorOrManagerFilterMixin, ListView):
    model = Message
    context_object_name = "email_schedule_messages"


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class MailingLogListView(ListView):
    model = MailingLog
    context_object_name = "log_schedule_messages"

    def get_queryset(self):
        q = super().get_queryset()
        if self.request.user.is_manager:
            return q
        return q.filter(Q(settings__creator=self.request.user))


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class ClientCreateView(AddCreatorMixin, LoginRequiredMixin, View):
    template_name = "mailing/message_form.html"
    form_class = CreateClientForm


@method_decorator(login_required(login_url="/auth/login/"), name="dispatch")
class MessageCreateView(AddCreatorMixin, LoginRequiredMixin, View):
    template_name = "mailing/message_form.html"
    form_class = CreateMessageForm


class EmailScheduleCreateView(AddFromCreatorMixin, LoginRequiredMixin, CreateView):
    model = EmailSchedule
    form_class = EmailScheduleForm
    success_url = reverse_lazy("mailing_list")


class EmailScheduleUpdateView(AddFromCreatorMixin, LoginRequiredMixin, UpdateView):
    model = EmailSchedule
    form_class = EmailScheduleForm
    success_url = reverse_lazy("mailing_list")
