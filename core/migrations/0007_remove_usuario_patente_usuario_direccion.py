# Generated by Django 4.2 on 2023-05-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pruebases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='patente',
        ),
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default='', max_length=50),
        ),
    ]
