# Generated by Django 3.0.10 on 2020-10-07 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id_primary', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('id_testcase', models.CharField(max_length=100)),
                ('testcase_title', models.CharField(max_length=100)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='feature.Feature')),
            ],
        ),
    ]
