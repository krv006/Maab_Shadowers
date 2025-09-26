from django.urls import path

from apps.views import AgentListAPIView

urlpatterns = [

    path('agent', AgentListAPIView.as_view(), name='agent'),
]
