from atexit import register
from django.contrib import admin

from core.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Historial)
admin.site.register(DetalleCompra)
admin.site.register(PruebasEs)
admin.site.register(UsuarioInvitado)
admin.site.register(TipoProducto)