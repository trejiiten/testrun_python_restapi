from rest_framework import serializers
from feature.models import Feature
from testcase.models import Testcase
from testcase.serializers import TestcaseSerializer
from environment.serializers import EnvironmentSerializer

class FeatureSerializer(serializers.ModelSerializer):
    testcases = TestcaseSerializer(many=True, read_only=True)
    environment = EnvironmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feature
        fields = '__all__'

    # def create(self, validated_data):
    #     testcases_data = validated_data.pop('testcases')
    #     feature = Feature.objects.create(**validated_data)
    #     for testcase_data in testcases_data:
    #         Testcase.objects.create(feature=feature, **testcase_data)
    #     return feature