from django.shortcuts import render, redirect
from .models import *
from .Carrito import *
from django.contrib import messages
# from .forms import UserRegisterForm
from django.shortcuts import render

from .models import *
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


def pago(request,):
    return render(request,'core/pago.html'  )

def micuenta(request):
    return render(request,'core/micuenta.html'  )

def historial(request):
    return render(request,'core/historial.html'  )

def contador(request):
    return render(request, 'core/contador.html')


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
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['email']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html
            newUser = Usuario(
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                email = request.POST['email'],
                pwd = request.POST['password'],
                tipo_usuario = False
            )
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    return render(request, 'core/registro.html')

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

def comprar(request):
    
    #newHistorial = Historial.objects.create( precio = precio ,fecha = datetime.now() )
    for key, value in request.session["carrito"].items():
        carrito = Carrito(request)
        carrito.limpiar()

    return render(request,'core/index.html')

def datoTransferencia(request):
    for key, value in request.session["carrito"].items():
        carrito = Carrito(request)
        carrito.limpiar()
    return render(request,'core/datoTransferencia.html')

# def historial(request)
# compra = compra.objects

# elimina la sesion iniciada.
def cerrarSesion(request):
    del request.session['email']
    request.session.modified = True
    messages.success(request, 'Sesion Cerrada')
    return render(request, 'core/index.html')


#Guarda datos del usario elegido.

def confirmarDatos(request):
    nombre = request.POST['nombreEs'] 
    apellido = request.POST['apellidoEs'] 
    user= request.session['email']
    telefono = request.POST['telefono']
    codigoPostal = request.POST['codigoPostal']
    estado = request.POST['estado']
    ciudad = request.POST['ciudad']
    rut = request.POST['rut']
    direccion = request.POST['direccion']
    newPruebasEs = PruebasEs(user = user, nombreEs = nombre, apellidoEs = apellido ,telefono = telefono, codigoPostal = codigoPostal, estado = estado , ciudad = ciudad , direccion = direccion)
    newUser = Usuario.objects.get(email = user)
    newUser.rut = rut
    newUser.direccion = direccion
    print("funca")
    newUser.save()
    newPruebasEs.save()
    return redirect('index')

# def transferencia(request):
#     for key, value in request.session["carrito"].items():
#         carrito = Carrito(request)
#         carrito.limpiar()
#     return redirect( request, 'core/datoTransferencia.html')




def historial_compras(request):
    compras = historial.objects.filter(usuario=request.user).order_by('-fecha_compra')
    return render(request, 'historial.html', {'compra': compras})



def editar(request, email = id):
    usuario = usuario.objects.get(id = email)
    if request.method == 'POST':
        form = usuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')
        
