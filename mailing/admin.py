from django.contrib import admin
from mailing.models import Client, Message, EmailSchedule, MailingLog


@admin.register(EmailSchedule)
class EmailScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "send_time",
        "interval",
        "status",
        "display_clients",
        "creator",
        "message",
    )
    list_filter = ("status",)
    search_fields = "status", "interval"

    def display_clients(self, obj):
        return ", ".join([str(client) for client in obj.clients.all()])

    display_clients.short_description = "Клиенты"


admin.site.register(Client)
admin.site.register(Message)
admin.site.register(MailingLog)
