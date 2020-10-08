from rest_framework import serializers
from testcase_step.models import TestcaseStep

class TestcaseStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestcaseStep
        fields = '__all__'