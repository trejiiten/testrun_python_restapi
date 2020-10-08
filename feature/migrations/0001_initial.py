# Generated by Django 3.0.10 on 2020-10-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id_primary', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('feature_file_title', models.CharField(max_length=100)),
                ('feature_file_type', models.CharField(max_length=100)),
                ('feature_file_location', models.CharField(max_length=255)),
                ('total_tests', models.CharField(max_length=255)),
                ('total_steps', models.CharField(max_length=255)),
                ('time_start', models.CharField(max_length=255)),
                ('time_end', models.CharField(max_length=255)),
                ('total_time', models.CharField(max_length=255)),
            ],
        ),
    ]
