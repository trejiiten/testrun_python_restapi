from rest_framework import serializers
from testcase.models import Testcase
from testcase_step.models import TestcaseStep
from testcase_step.serializers import TestcaseStepSerializer

class TestcaseSerializer(serializers.ModelSerializer):
    testcase_steps = TestcaseStepSerializer(many=True, read_only=True)
    
    class Meta:
        model = Testcase
        fields = '__all__'

    # def create(self, validated_data):
    #     testcase_steps_data = validated_data.pop('testcase_steps')
    #     testcase = Testcase.objects.create(**validated_data)
    #     for testcase_step_data in testcase_steps_data:
    #         TestcaseStep.objects.create(testcase=testcase, **testcase_step_data)
    #     return testcase