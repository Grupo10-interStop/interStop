# Generated by Django 2.0.5 on 2020-07-16 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interStop_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='testprueba',
        ),
        migrations.RemoveField(
            model_name='ubicacion',
            name='id_departamento',
        ),
        migrations.RemoveField(
            model_name='ubicacion',
            name='id_municipio',
        ),
        migrations.DeleteModel(
            name='Ubicacion',
        ),
    ]
