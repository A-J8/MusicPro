from django.shortcuts import render, redirect
from .models import *
from .Carrito import *
from .forms import UserRegisterForm
# Create your views here.

def index(request):
    contexto = {'productos' : Producto.objects.all()}
    return render(request,'core/index.html', contexto)

def producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'producto': producto
    }
    return render(request, 'core/producto.html', data)

def carrito(request):
    return render(request,'core/carrito.html'  )


def pago(request):
    return render(request,'core/pago.html'  )

def historial(request):
    return render(request,'core/historial.html'  )


#inicio de sesion del usuario registrado
def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email
            return redirect('index')
        except Usuario.DoesNotExist as e: 
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'core/login.html')
    


#registra y valida un nuevo usuario
def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('/')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'core/registro.html', context)

def administrador(request):
    return render(request,'core/administrador.html'  )    

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
    
    #newHistorial = Historial.objects.create( precio = precio ,fecha = datetime.now() )
    for key, value in request.session["carrito"].items():
        carrito = Carrito(request)
        carrito.limpiar()

    return redirect('carrito')

#def historial(request)
#compra = compra.objects