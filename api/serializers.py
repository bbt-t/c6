from rest_framework import serializers

from mailing.models import EmailSchedule, Client, Message


class EmailScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSchedule
        exclude = ("creator",)
        read_only_fields = ("id", "creator")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ("creator",)
        read_only_fields = ("id", "creator")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ("creator",)
        read_only_fields = ("id", "creator")
