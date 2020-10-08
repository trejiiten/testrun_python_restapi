from testcase.models import Testcase
from rest_framework import viewsets, permissions
from .serializers import TestcaseSerializer

class TestcaseViewSet(viewsets.ModelViewSet):
    queryset = Testcase.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestcaseSerializer