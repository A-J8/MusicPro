# Generated by Django 4.1.3 on 2023-05-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_usuario_cam_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cam_auto',
            field=models.IntegerField(default=0),
        ),
    ]