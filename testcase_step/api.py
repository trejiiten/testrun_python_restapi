from testcase_step.models import TestcaseStep
from rest_framework import viewsets, permissions
from .serializers import TestcaseStepSerializer

class TestcaseStepViewSet(viewsets.ModelViewSet):
    queryset = TestcaseStep.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestcaseStepSerializer