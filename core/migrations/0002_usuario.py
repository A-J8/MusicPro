# Generated by Django 4.1.5 on 2023-04-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=16)),
                ('apellido', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('pwd', models.CharField(max_length=12)),
                ('tipo_usuario', models.BooleanField(default=False, max_length=16)),
                ('rut', models.CharField(default=0, max_length=10)),
                ('patente', models.CharField(default=0, max_length=8)),
            ],
        ),
    ]
