from feature.models import Feature
from rest_framework import viewsets, permissions
from .serializers import FeatureSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FeatureSerializer