# Generated by Django 2.0.1 on 2018-11-18 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_patient_detail_labuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_detail',
            name='LabUser',
        ),
        migrations.AddField(
            model_name='patient_detail',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
