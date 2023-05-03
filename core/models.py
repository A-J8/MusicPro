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


# Create models Usuario.
class Usuario(models.Model):
    nombre = models.CharField(max_length=16, )
    apellido = models.CharField( max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    pwd = models.CharField(null=False, max_length=12)
    tipo_usuario = models.BooleanField( max_length=16, default=False)
    rut = models.CharField(max_length=10, default=0)
    patente = models.CharField(max_length=8, default=0)


# create models historial

class Historial(models.Model):
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=40)
    envio = models.CharField(max_length=40)