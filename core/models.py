from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    imagen =models.ImageField(upload_to='media/')
    descripcion = models.CharField(max_length=500, default='')
    def __str__(self):
        return f'{self.nombre}'