# Generated by Django 3.2.7 on 2021-11-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0009_auto_20211109_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='n_reunion',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
