# Generated by Django 4.2 on 2023-05-15 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='tipo_usuario',
            new_name='tipoUsuario',
        ),
    ]
