# Generated by Django 4.1.2 on 2023-06-14 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_listamodels_disciplina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listamodels',
            name='data',
        ),
        migrations.RemoveField(
            model_name='listamodels',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='listamodels',
            name='modificado_em',
        ),
    ]