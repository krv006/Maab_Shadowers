from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.models import Agents
from apps.serializer import AgentModelSerializer


class AgentListAPIView(ListAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentModelSerializer
    permission_classes = AllowAny,
