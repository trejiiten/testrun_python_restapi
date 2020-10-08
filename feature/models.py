from django.db import models

class Feature(models.Model):
    id_primary = models.AutoField(primary_key=True, null=False, auto_created=True)
    feature_file_title = models.CharField(max_length=100)
    feature_file_type = models.CharField(max_length=100)
    feature_file_location = models.CharField(max_length=255)
    total_tests = models.CharField(max_length=255)
    total_steps = models.CharField(max_length=255)
    time_start = models.CharField(max_length=255)
    time_end = models.CharField(max_length=255)
    total_time = models.CharField(max_length=255)