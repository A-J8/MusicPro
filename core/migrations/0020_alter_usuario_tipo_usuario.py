# Generated by Django 4.2 on 2023-05-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_detallecompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.IntegerField(),
        ),
    ]
