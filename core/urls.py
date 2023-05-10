from .views import *
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', index, name="index"),
    path('producto/<int:id>', producto, name="producto"),
    path('carrito', carrito, name="carrito"),
    path('pago/<email>', pago, name="pago"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('administrador', administrador, name="administrador"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('micuenta', micuenta, name="micuenta"),
    path('historial', historial, name="historial"),
    path('contador', contador, name="contador"),
    path('comprar', comprar, name="comprar"),
    path('datoTransferencia', datoTransferencia, name="datoTransferencia"),

    path('confirmarDatos/<nombre>',confirmarDatos, name="confirmarDatos"),

    #funciones del carrito
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="cls"),
    path('comprar', comprar, name="comprar"),

    #funciones contador
    path('cambiarEstadoPago/<int:id>', cambiarEstadoPago, name="cambiarEstadoPago"),




    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })  

    

]

