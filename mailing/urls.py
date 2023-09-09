from django.urls import path

from .views import (
    ClientListView,
    EmailScheduleListView,
    MessageListView,
    ClientCreateView,
    MessageCreateView,
    EmailScheduleCreateView,
    EmailScheduleUpdateView,
    MailingLogListView,
)

urlpatterns = [
    path("mailing_list/", EmailScheduleListView.as_view(), name="mailing_list"),
    path("clients/", ClientListView.as_view(), name="clients"),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("mailing_log", MailingLogListView.as_view(), name="mailing_log"),
    path("add_client/", ClientCreateView.as_view(), name="add_client"),
    path("add_msg/", MessageCreateView.as_view(), name="add_msg"),
    path(
        "add_email_schedule/",
        EmailScheduleCreateView.as_view(),
        name="add_email_schedule",
    ),
    path(
        "edit_email_schedule/<pk>",
        EmailScheduleUpdateView.as_view(),
        name="add_email_schedule",
    ),
]
