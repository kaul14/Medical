# Generated by Django 2.0.1 on 2018-11-23 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_medical_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical_library',
            name='prevention',
        ),
    ]