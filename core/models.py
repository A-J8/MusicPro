from django.db import models
from django.forms import ModelForm
from multiprocessing.dummy import Value

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=40)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    imagen =models.ImageField(upload_to='media/')
    descripcion = models.CharField(max_length=500, default='')
    idTipoProducto = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nombre}'
  

# Create models Usuario.
class Usuario(models.Model):
    cam_auto = models.IntegerField(default=0)
    nombre = models.CharField(max_length=16, )
    apellido = models.CharField( max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    pwd = models.CharField(null=False, max_length=12)
    tipoUsuario = models.IntegerField()                        
    rut = models.CharField(max_length=10, default= '')
    direccion = models.CharField(max_length=50, null=False, default= '')
    telefono = models.CharField(max_length=10, default=0)
    codigoPostal = models.IntegerField(max_length=50, default= 0)
    estado = models.CharField(max_length=50, default= '')
    ciudad = models.CharField(max_length=50, default= '')
    def save(self, *args, **kwargs):
        if not self.cam_auto:
            last_object = Usuario.objects.order_by('-cam_auto').first()
            self.cam_auto = 1 if not last_object else last_object.cam_auto + 1
        super().save(*args, **kwargs)
   


class UsuarioInvitado(models.Model):
    nombre = models.CharField(max_length=16, )
    apellido = models.CharField( max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    rut = models.CharField(max_length=10, default= '')
    direccion = models.CharField(max_length=50, null=False, default= '')
    telefono = models.CharField(max_length=10, default=0)
    codigoPostal = models.IntegerField(max_length=50, default= 0)
    estado = models.CharField(max_length=50, default= '')
    ciudad = models.CharField(max_length=50, default= '')

class Historial(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    estadoPago = models.BooleanField(default=False)
    estadoEnvio = models.BooleanField(default=False)
    OPCION_1 = 'Transferencia'
    OPCION_2 = 'Transbank'
    OPCIONES_TIPO_PAGO = [
        (True, OPCION_1),
        (False, OPCION_2),
    ]
    tipoPago = models.BooleanField(choices=OPCIONES_TIPO_PAGO, default=False)
    TIPO_1 = 'Logueado'
    TIPO_2 = 'Invitado'
    OPCIONES_TIPO_USUARIO = [
        (True, TIPO_1),
        (False, TIPO_2),
    ]
    tipoUsuario = models.BooleanField(choices=OPCIONES_TIPO_USUARIO, null=False,  default=False)
    email = models.EmailField(null=False, default='')

class DetalleCompra(models.Model):
    idHistorial = models.IntegerField()
    idProducto = models.IntegerField()
    cantidad = models.IntegerField()


# #ejemplo en prueba
class PruebasEs(models.Model):
    user = models.EmailField(primary_key=True, max_length=50)
    nombreEs = models.CharField( max_length=50, null=False,default= '')
    apellidoEs = models.CharField( max_length=50, null=False,default= '')
    telefono = models.CharField(max_length=10, default=0)
    codigoPostal = models.IntegerField( default= 0)
    rut = models.CharField(max_length=10, default=0)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)





