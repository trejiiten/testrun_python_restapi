from environment.models import Environment
from rest_framework import viewsets, permissions
from .serializers import EnvironmentSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EnvironmentSerializer