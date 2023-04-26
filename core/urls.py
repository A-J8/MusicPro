from .views import *
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', index, name="index"),
    path('carrito', carrito, name="carrito"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('admin', admin, name="admin"),


    #funciones del carrito
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="cls"),
    path('comprar/<int:precio>', comprar, name="comprar"),


    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })  
]
