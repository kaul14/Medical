# Generated by Django 2.0.1 on 2018-11-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20181117_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_detail',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]