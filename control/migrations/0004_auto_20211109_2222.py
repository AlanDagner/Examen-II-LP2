# Generated by Django 3.2.7 on 2021-11-10 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20211109_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='hora_llegada',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='llego',
        ),
    ]
