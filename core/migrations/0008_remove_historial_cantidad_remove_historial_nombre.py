# Generated by Django 4.2 on 2023-05-10 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_usuario_patente_usuario_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historial',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='historial',
            name='nombre',
        ),
    ]