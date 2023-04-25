from django.shortcuts import render, redirect
from .models import *
from .Carrito import *
# Create your views here.

def index(request):
    contexto = {'productos' : Producto.objects.all()}
    return render(request,'core/index.html', contexto)

def carrito(request):
    return render(request,'core/carrito.html'  )

def login(request):
    return render(request,'core/login.html'  )
def registro(request):
    return render(request,'core/registro.html'  )
def admin(request):
    return render(request,'core/admin.html'  )    

#funciones del carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
        carrito.agregar(producto) 
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    if producto.stock >= 0:
        producto.stock += 1
        producto.save()
        carrito.restar(producto)
    return redirect("carrito")

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def comprar(request, precio):
    #codigo = 0
    #codigo = precio *99/234
    #newHistorial = Historial.objects.create( codigo =codigo  , precio = precio ,fecha = datetime.now() )
    for key, value in request.session["carrito"].items():
        carrito = Carrito(request)
        carrito.limpiar()

    return redirect('carrito')