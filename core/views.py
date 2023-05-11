from datetime import datetime, date
from django.shortcuts import render, redirect
from .models import *
from .Carrito import *
from .context_processor import total_carrito
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
    if "email" in request.session:
        usuario = Usuario.objects.filter(email = request.session['email'])
    else:
        usuario = 1
    return render(request,'core/carrito.html', {'usuario':usuario}  )


def pago(request, email):
    usuario = Usuario.objects.get(email = email)
    return render(request,'core/pago.html' ,  {'usuario':usuario})

def pagoInvitado1(request):
    return render(request,'core/pagoInvitado.html' )

def micuenta(request):
    return render(request,'core/micuenta.html'  )

def historial(request):
    return render(request,'core/historial.html'  )

def contador(request):
    contexto = {'historial' : Historial.objects.all()}
    return render(request, 'core/contador.html', contexto)

def historial(request):
    compras = Historial.objects.all().order_by('-fecha')
    return render(request, 'core/historial.html', {'compras': compras})



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
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            carrito.limpiar()
    return render(request, 'core/index.html')


#Guarda datos del usario elegido.

def confirmarDatos(request, email):
    if request.method == 'POST':
        print("funca0")
        newUser = Usuario.objects.get(email=email)
        
        newUser.rut = request.POST['rut'],
        newUser.telefono = request.POST['telefono'],
        newUser.direccion = request.POST['direccion'],
        newUser.ciudad = request.POST['ciudad'],
        newUser.estado = request.POST['estado'],
        newUser.codigoPostal = request.POST['codigo_postal']         
        
        print("funca1")
        newUser.save()
        
        total = 0
        if 'carrito' in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
        
        newHistorial = Historial(
            email= request.POST['email'],
            fecha = datetime.today(),
            total = total,
            tipoPago = True,
            tipoUsuario = True,
        )
        newHistorial.save()
        print("funca2")
        
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            carrito.limpiar()
        return redirect('datoTransferencia')
    else:
        print("nofunca3")
        return redirect('carrito')

def datoInvitado(request):
    if request.method == 'POST':
        newUserinvitado = UsuarioInvitado(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'], 
            email= request.POST['email'],
            rut = request.POST['rut'],
            telefono = request.POST['telefono'],
            direccion = request.POST['direccion'],
            ciudad = request.POST['ciudad'],
            estado = request.POST['estado'],
            codigoPostal = request.POST['codigo_postal']         
        )
        print("funca1")
        newUserinvitado.save()
        
        total = 0
        if 'carrito' in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
        
        newHistorial = Historial(
            email= request.POST['email'],
            fecha = datetime.today(),
            total = total,
            tipoPago = True,
            tipoUsuario = False,
        )
        newHistorial.save()
        print("funca2")
        
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            carrito.limpiar()
        return redirect('datoTransferencia')
    else:
        print("nofunca3")
        return redirect('carrito')
        
# def transferencia(request):
#     for key, value in request.session["carrito"].items():
#         carrito = Carrito(request)
#         carrito.limpiar()
#     return redirect( request, 'core/datoTransferencia.html')



def editar(request, email = id):
    usuario = usuario.objects.get(id = email)
    if request.method == 'POST':
        form = usuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')
        
#FUNCION CONTADOR
def cambiarEstadoPago(request, id):
    contexto = {'historial' : Historial.objects.all()}
    historial = Historial.objects.get(id=id)
    if historial.estadoPago == True:
        historial.estadoPago = False  # cambia el estado a lo opuesto
        historial.save()
    else:
        historial.estadoPago = True
        historial.save()
    return render(request, 'core/contador.html', contexto)

