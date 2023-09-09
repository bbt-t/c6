from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mailing.mixins import CreatorOrManagerFilterMixin
from .permissions import IsVerify
from .serializers import EmailScheduleSerializer, ClientSerializer
from mailing.models import EmailSchedule, Client


class MailingViewSet(CreatorOrManagerFilterMixin, ModelViewSet):
    queryset = EmailSchedule.objects.all()
    serializer_class = EmailScheduleSerializer
    permission_classes = [IsAuthenticated, IsVerify]


class ClientsViewSet(CreatorOrManagerFilterMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsVerify]
