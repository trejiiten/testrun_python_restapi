from feature.models import Feature
from django.db import models
from feature.models import Feature

class Testcase(models.Model):
    id_primary = models.AutoField(primary_key=True, null=False, auto_created=True)
    feature = models.ForeignKey(Feature, related_name='testcases', on_delete=models.CASCADE)
    id_testcase = models.CharField(max_length=100)
    testcase_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.id_testcase