# Generated by Django 4.2.1 on 2023-05-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_remove_historial_estadostock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='estadoStock',
            field=models.BooleanField(null=True),
        ),
    ]