from django.db import models
from django.db.models.deletion import CASCADE
from feature.models import Feature

class Environment(models.Model):
    id_primary = models.AutoField(primary_key=True, null=False, auto_created=True)
    feature = models.ForeignKey(Feature, related_name='environment', on_delete=models.CASCADE)
    os_name = models.CharField(max_length=50)
    os_version = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    platform_architecture = models.CharField(max_length=20)
    user = models.CharField(max_length=30)
    host = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    environment = models.CharField(max_length=10)
    browser_name = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50)
    headless_mode = models.CharField(max_length=50)
    awsdev = models.CharField(max_length=50)
    java_version = models.CharField(max_length=50)
    jvm_version = models.CharField(max_length=50)
    jvm_vendor = models.CharField(max_length=100)
    webdriver_version = models.CharField(max_length=50)

