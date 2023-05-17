from .views import *
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', index, name="index"),
    path('filtrar/<int:id>', filtrar, name="filtrar"),

    path('producto/<int:id>', producto, name="producto"),
    path('carrito', carrito, name="carrito"),
    
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('administrador', administrador, name="administrador"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('micuenta', micuenta, name="micuenta"),
    path('historial', historial, name="historial"),
    path('contador', contador, name="contador"),
    path('comprar', comprar, name="comprar"),
    path('datoTransferencia', datoTransferencia, name="datoTransferencia"),
    path('vendedor/',vendedor, name="vendedor"),

    #funcion perfil
    
    path('perfil/',perfil, name="perfil"),
    path('editar_perfil/<email>', editar_perfil, name="editar_perfil"),
    path('actualizarPerfil/<email>', actualizarPerfil, name='actualizarPerfil'),

    path('pago/<email>', pago, name="pago"),
    path('confirmarDatos/<email>',confirmarDatos, name="confirmarDatos"),
    
    
    path('pagoInvitado1/',pagoInvitado1, name="pagoInvitado1"),
    path('datoInvitado/',datoInvitado, name="datoInvitado"),

    #funciones del carrito
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="cls"),
    path('comprar', comprar, name="comprar"),

    #funciones contador
    path('cambiarEstadoPago/<int:id>', cambiarEstadoPago, name="cambiarEstadoPago"),
    path('cambiarEstadoEnvio/<int:id>', cambiarEstadoEnvio, name="cambiarEstadoEnvio"),

    #funciones bodeguero
    path('bodeguero', bodeguero, name="bodeguero"),
    path('bodegueroStock', bodegueroStock, name="bodegueroStock"),
    path('cambiarEstadoStock/<int:id>', cambiarEstadoStock, name="cambiarEstadoStock"),
    path('SinStock/<int:id>', SinStock, name="SinStock"),
    path('ConStock/<int:id>', ConStock, name="ConStock"),
    path('ActualizarStock/', ActualizarStock, name="ActualizarStock"),

    #funciones de administrador
    path('usuarioAdmin', usuarioAdmin, name="usuarioAdmin"),
    path('crudUsuario', crudUsuario, name="crudUsuario"),
    path('eliminarUsuario/<email>', eliminarUsuario, name="eliminarUsuario"),
    path('EditarUsuario', EditarUsuario, name='EditarUsuario'),
    path('EditarUsuario/<email>', EditarUsuario, name='EditarUsuario'),
    path('editar_usuario', editar_usuario, name='editar_usuario'),
    path('actualizarUsuario/<email>', actualizarUsuario, name='actualizarUsuario'),
    # path('fromUsuario', fromUsuario, name="fromUsuario"),
    path('repVentas', repVentas, name="repVentas"),
    path('repdesptienda', repdesptienda, name="repdesptienda"),
    path('repestrVentas', repestrVentas, name="repestrVentas"),


    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })  

    

]

