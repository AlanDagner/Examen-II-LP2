# Generated by Django 3.2.7 on 2021-11-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='cantidad_por_sede',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='n_reunion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='socio',
            name='codigo',
            field=models.IntegerField(),
        ),
    ]
