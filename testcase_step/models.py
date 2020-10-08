from django.db import models
from testcase.models import Testcase

class TestcaseStep(models.Model):
    id_primary = models.AutoField(primary_key=True, null=False, auto_created=True)
    testcase = models.ForeignKey(
        Testcase, related_name='testcase_steps', on_delete=models.CASCADE)
    id_testcase_step = models.CharField(max_length=10)
    testcase_step_title = models.CharField(max_length=100)
    testcase_step_status = models.CharField(max_length=100)
    error_message = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.id_testcase_step
