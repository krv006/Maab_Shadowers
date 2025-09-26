from rest_framework.serializers import ModelSerializer

from apps.models import Agents


class AgentModelSerializer(ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'
