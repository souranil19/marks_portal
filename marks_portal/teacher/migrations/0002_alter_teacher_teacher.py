# Generated by Django 5.2.4 on 2025-07-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher',
            field=models.CharField(max_length=20),
        ),
    ]
