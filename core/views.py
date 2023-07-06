from datetime import datetime, date
from django.shortcuts import render, redirect, reverse
from .models import *
from .Carrito import *
from .context_processor import total_carrito
from django.contrib import messages
# from .forms import UserRegisterForm
from django.shortcuts import render
from .models import *
from .models import DetalleCompra
import requests
from .apibanco import obtener_valor_dolar
from django.http import JsonResponse
import json
# Create your views here.

#API del tiempo
from .apiTiempo import get_weather_data
import locale
from django.conf import settings
from rest_framework import generics
from .serializers import ProductoSerializer

def index(request):
    api_key = "7a57daf636775b047f328f8d78cf057a"
    #Coordenadas de Simulacion Local de Melipilla
    lat = -33.685983770235346
    lon = -71.21694948040461
    weather_data = get_weather_data(api_key, lat, lon)
    print(weather_data)

    fecha_actual = datetime.now()
    # Configurar la localización en español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    # Formatear la fecha en español
    fecha_formateada = fecha_actual.strftime('%A %d de %B')

    contexto = {
        'productos' : Producto.objects.all(),
        'tipoProducto' : TipoProducto.objects.all(),
        "weather_data": weather_data,
        "fecha": fecha_formateada
        }
    print(date)
    return render(request,'core/index.html', contexto)

def filtrar(request, id):
    productos = Producto.objects.filter(idTipoProducto=id)
    tipoProductos = TipoProducto.objects.all()

    contexto = {
        'productos': productos,
        'tipoProducto': tipoProductos
    }
    return render(request, 'core/index.html', contexto)

def producto(request, id):
    
    data = {
        'producto' : Producto.objects.get(id=id),
        'tipoProducto' : TipoProducto.objects.all()
    }
    return render(request, 'core/producto.html', data)

def carrito(request):
    if "email" in request.session:
        usuario = Usuario.objects.filter(email = request.session['email'])
    else:
        usuario = 1
    return render(request,'core/carrito.html', {'usuario':usuario}  )


def pago(request, email):
    fecha =  datetime.now().strftime('%Y-%m-%d')
    api_key = "user=211730625&pass=uVYeQQAvWY3J"
    serie1 = "F073.TCO.PRE.Z.D"
    dolar = obtener_valor_dolar(fecha, api_key,serie1)
    total = 0
    cantidadTotal = 0
    mensaje = "Al estar registrado por compras con mas de 4 productos usted obtiene un descuento del 10%"
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            total += int(value["acumulado"])
            cantidadTotal += int(value["cantidad"])
            if cantidadTotal > 4:
                    total = total * 0.9
                    mensaje = "Usted tiene un descuento del 10% por estar registrado y hacer una compra de mas de 4 productos!"
    usuario = Usuario.objects.get(email = email)

     
    series = dolar['Series']
    obs = series['Obs']
    cero = obs[0]
    value = cero["value"]
    valor_dolar = float(value)
    print( value)
    total_dolar = round(total / valor_dolar, 2)
    data = {
        'usuario': usuario,
        'totalD' : total,
        'total_dolar' : total_dolar,
        'mensaje' : mensaje,
        'dolar' : dolar
    }
    return render(request,'core/pago.html' ,  data)


def bandas(request):
    resultado = requests.get("http://127.0.0.1:5000/bandas")
    bandas = resultado.json()
    data = {'bandas':bandas}
    return render(request,'core/bandas.html', data)

def pagoInvitado1(request):
    fecha =  datetime.now().strftime('%Y-%m-%d')
    api_key = "user=211730625&pass=uVYeQQAvWY3J"
    serie1 = "F073.TCO.PRE.Z.D"
    dolar = obtener_valor_dolar(fecha, api_key,serie1)

    total = 0
    cantidadTotal = 0
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            total += int(value["acumulado"])
            cantidadTotal += int(value["cantidad"])

    series = dolar['Series']
    obs = series['Obs']
    cero = obs[0]
    value = cero["value"]
    valor_dolar = float(value)
    print( value)
    total_dolar = round(total / valor_dolar, 2)

    dolar = {
        'dolar' : dolar,
        'total_dolar' : total_dolar
    }
    return render(request,'core/pagoInvitado.html', dolar)

def perfil(request):
    return render(request,'core/perfil.html' )

def micuenta(request):
    return render(request,'core/micuenta.html'  )

def contador(request):
    contexto = {'historial' : Historial.objects.all()}
    return render(request, 'core/contador.html', contexto)

def historial(request):
    contexto = {
        'compras' : Historial.objects.filter(email = request.session['email']).order_by('-fecha'),
        'detalle' : DetalleCompra.objects.all(),
        'producto' : Producto.objects.all()
    }
    return render(request, 'core/historial.html', contexto)

def vendedor(request):
    contexto = {
        'compras' : Historial.objects.all().order_by('-fecha'),
        'detalle' : DetalleCompra.objects.all(),
        'producto' : Producto.objects.all()
        }
    
    return render(request, 'core/vendedor.html', contexto)




#inicio de sesion del usuario registrado
def login(request):
    # Ejemplo de definición de variable
    usuarioNotFound = True
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email
            request.session['nombre'] = newUser.nombre
            request.session['apellido'] = newUser.apellido
            request.session['tipoUsuario'] = newUser.tipoUsuario
            if newUser.tipoUsuario == 1:
                return redirect('administrador')
            elif newUser.tipoUsuario == 2:
                return redirect('contador')
            elif newUser.tipoUsuario == 3:
                return redirect('index')
            elif newUser.tipoUsuario == 4:
                return redirect('bodeguero')           
            else:
                messages.success(request, 'Operación exitosa')
                return redirect('index')
        except Usuario.DoesNotExist as e: 
            messages.success(request, 'Correo o constraseña no son correctos')
            messages.error(request, 'Ocurrió un error')
            usuarioNotFound = False
    return render(request, 'core/login.html', {'usuarioNotFound' : usuarioNotFound})





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
                tipoUsuario = False
            )
            
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    return render(request, 'core/registro.html')


#funciones de administrador
def administrador(request):
    return render(request,'core/administrador.html'  ) 

def usuarioAdmin(request): 
    contexto = {'usuario': Usuario.objects.all()}
    return render(request,'core/usuariosAdmin.html' , contexto ) 

def crudUsuario(request):
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
                tipoUsuario = False
            )
            
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('usuarioAdmin')
    return render(request,'core/crudUsuarioad.html' )
# Funcion de editar usuarios del admin
def EditarUsuario(request, email):
    contexto = {'usuario' : Usuario.objects.get(email=email)}
    return render(request, 'core/actualizarUsuarioAdmin.html', contexto)

# Funcion de actulizar el usuario como admin
def actualizarUsuario(request, email):
    usuario = Usuario.objects.get(email = email)
    return render(request, 'core/micuenta.html', {'usuario':usuario})

# Funcion para poder editar el usuario como admin
def editar_usuario(request):
        tipoUsuario = request.POST['tipoUsuario']
        nombre = request.POST['nombre']
        email = request.POST['email']
        apellido = request.POST['apellido']
        password = request.POST['password']
        
        oldemail = Usuario.objects.get(email = email) 
        oldemail.tipoUsuario = tipoUsuario
        oldemail.nombre = nombre
        oldemail.apellido = apellido
        oldemail.pwd = password
        oldemail.save()
        print("Usuario invitado actualizado con éxito.")
        return redirect('usuarioAdmin')

 #elimina al usario por el id (funcion de admin).
def eliminarUsuario(request, email):
    
        usuario = Usuario.objects.get(email=email)
        usuario.delete()
        return redirect('usuarioAdmin')
    # return render ( request,'core/usuariosAdmin.html' )

def repVentas(request):
    contexto = {'historial': Historial.objects.all()}
    return render(request, 'core/repVentas.html' ,contexto)

def repdesptienda(request):
    # contexto = {'historial': Historial.objects.all()}
    # historial = Historial.objects.all()
    # contexto= [{'total': item.total} for item in historial]
    # return JsonResponse(datos_formateados, safe=False)
    return render(request,'core/repdesempeñotienda.html'  ) 

def repestrVentas(request):
    return render(request,'core/repestrategiaVentas.html'  ) 

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

    api_key = "7a57daf636775b047f328f8d78cf057a"
    #Coordenadas de Simulacion Local de Melipilla
    lat = -35.80323780506383
    lon = -71.8884938534825
    weather_data = get_weather_data(api_key, lat, lon)
    print(weather_data)

    fecha_actual = datetime.now()
    # Configurar la localización en español
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    # Formatear la fecha en español
    fecha_formateada = fecha_actual.strftime('%A %d de %B')

    contexto = {
        'productos' : Producto.objects.all(),
        'tipoProducto' : TipoProducto.objects.all(),
        "weather_data": weather_data,
        "fecha": fecha_formateada
        }
    
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            carrito.limpiar()
    return render(request, 'core/index.html', contexto)


#Guarda datos del usario elegido.

def confirmarDatos(request, email):
    if request.method == 'POST':
        newUser = Usuario.objects.get(email=email)
        
        newUser.rut = request.POST['rut'],
        newUser.telefono = request.POST['telefono'],
        newUser.direccion = request.POST['direccion'],
        newUser.ciudad = request.POST['ciudad'],
        newUser.estado = request.POST['estado'],
        newUser.codigoPostal = request.POST['codigo_postal']         
        newUser.save()
        
        metodoPago = request.POST.get('metodoPago')
        cantidadTotal = 0
        total = 0
        if 'carrito' in request.session:
             for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
                cantidadTotal += int(value["cantidad"])
                if cantidadTotal > 4:
                    total = total * 0.9
        if metodoPago == '1':
            url_destino = reverse('CrearTransaccion') + '?monto=' + str(total)
            return redirect(url_destino)
        
        elif metodoPago == '2': 
            newHistorial = Historial(
                email = request.POST['email'],
                fecha = datetime.today(),
                total = total,
                tipoPago = True,
                tipoUsuario = True,
            )
            newHistorial.save()
            
            for key, value in request.session["carrito"].items():
                carrito = Carrito(request)
                newDetalle = DetalleCompra(
                    idHistorial = newHistorial.id,
                    idProducto = value["producto_id"],
                    cantidad = value["cantidad"]
                )
                newDetalle.save()

            for key, value in request.session["carrito"].items():
                carrito = Carrito(request)
                carrito.limpiar()
            return redirect('datoTransferencia')
        else:
            return redirect('contador')
    else:
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
        request.session['email'] = request.POST['email']
         
        metodoPago = request.POST.get('metodoPago')
        
        if metodoPago == '1':
            url_destino = reverse('CrearTransaccion') + '?monto=' + str(total)
            return redirect(url_destino)
        
        elif metodoPago == '2': 
            for key, value in request.session["carrito"].items():
                carrito = Carrito(request)
                newDetalle = DetalleCompra(
                    idHistorial = newHistorial.id,
                    idProducto = value["producto_id"],
                    cantidad = value["cantidad"]
                )
                newDetalle.save()

            for key, value in request.session["carrito"].items():
                carrito = Carrito(request)
                carrito.limpiar()
            return redirect('datoTransferencia')
    else:
        print("nofunca3")
        return redirect('carrito')
        

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

def cambiarEstadoEnvio(request, id):
    contexto = {'historial' : Historial.objects.all()}
    historial = Historial.objects.get(id=id)
    if historial.estadoEnvio == True:
        historial.estadoEnvio = False  # cambia el estado a lo opuesto
        historial.save()
    else:
        historial.estadoEnvio = True
        historial.save()
    return render(request, 'core/contador.html', contexto)

#funciones bodeguero
def bodeguero(request):
    print("funca")
    contexto = {
        'detalleCompra': DetalleCompra.objects.all(),
        'producto': Producto.objects.all(),
        'historial': Historial.objects.all()
    }
    return render(request,'core/bodeguero.html', contexto)

def bodegueroStock(request):
    contexto = {
        'productos' : Producto.objects.all()
    }
    return render(request,'core/bodegueroStock.html', contexto)

def ActualizarStock(request):
    contexto = {
        'productos' : Producto.objects.all()
    }
    id = request.POST['id']
    NewStock = int(request.POST['NewStock'])

    oldStock =Producto.objects.get(id = id) 
    oldStock.stock = oldStock.stock + NewStock
    if oldStock.stock >= 0:
        oldStock.save()
    else:
        messages.success(request, 'No puede ser menor a 0')
    return render(request, 'core/bodegueroStock.html', contexto)

def cambiarEstadoStock(request, id):
    
    contexto = {
        'detalleCompra': DetalleCompra.objects.all()
    }
    detalleCompra = DetalleCompra.objects.get(id=id)
    if detalleCompra.estadoStock == 0:
        detalleCompra.estadoStock = 1
        
    elif detalleCompra.estadoStock == 1:
        detalleCompra.estadoStock = 0
    
    detalleCompra.save()
    return render(request, 'core/bodeguero.html', contexto)

def SinStock(request, id):
    contexto = {
        'detalleCompra': DetalleCompra.objects.all()
    }
    detalleCompra = DetalleCompra.objects.get(id=id)
    detalleCompra.estadoStock = 2
    detalleCompra.save()
    return render(request, 'core/bodeguero.html', contexto)

def ConStock(request, id):
    contexto = {
        'detalleCompra': DetalleCompra.objects.all()
    }
    detalleCompra = DetalleCompra.objects.get(id=id)
    detalleCompra.estadoStock = 0
    detalleCompra.save()
    return render(request, 'core/bodeguero.html', contexto)


def perfil(request):
    usuario = Usuario.objects.filter(email = request.session['email'])
    return render(request, 'core/perfil.html', {'usuario':usuario})

def actualizarPerfil(request, email):
    usuario = Usuario.objects.get(email = email)
    return render(request, 'core/micuenta.html', {'usuario':usuario})

def editar_perfil(request, email):
        
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['password']
        
      
        oldemail = Usuario.objects.get(email = request.session['email']) 
        oldemail.nombre = nombre
        oldemail.apellido = apellido
        oldemail.pwd = password
        oldemail.save()
        print("Usuario invitado actualizado con éxito.")
        return redirect('perfil')
    
import random

def generarNumero():
    numero_aleatorio = random.randint(1, 10000000) 
    return numero_aleatorio

# TRANSBANK
from transbank.webpay.webpay_plus.transaction import Transaction

def CrearTransaccion(request):
    monto = request.GET.get('monto')
    email = request.session['email']
    numero = generarNumero()
    buy_order = str(numero)

    amount = round(float(monto), 2) 
    session_id = email
    # Crear una instancia de la transacción
    transaction = Transaction()
    # Llamar al método create() en la instancia de transacción
    response = transaction.create(
        buy_order= buy_order,
        session_id=session_id,
        amount=amount,
        return_url='http://localhost:8000/webpay/RetornoTransaccion/'
    )
    token = response.get("token")
    url = response.get("url")
    
    redirect_url = f"{url}?token_ws={token}"

    # Redirigir al usuario a la URL de pago de Transbank
    return redirect(redirect_url)


def RetornoTransaccion(request): #esta tienen los errores en request
    token_ws = request.GET.get('token_ws')  # Obtener el token de la transacción desde la URL
    if not token_ws:
        return redirect('pagoFallido') 
    transaction = Transaction()
    resp = transaction.commit(token_ws)

    estado = resp.get('status')
    fechaISO8601 = resp.get('transaction_date')
    fecha_hora = datetime.strptime(fechaISO8601, '%Y-%m-%dT%H:%M:%S.%fZ') # Analiza la fecha
    fecha = fecha_hora.strftime('%d-%m-%Y %H:%M:%S') #Seteo del nuevo formato
    
    try:
        tipoUsuario = request.session['tipoUsuario'] #para error
    except KeyError:
        tipoUsuario = 0

   
    if tipoUsuario <= 0:
        TUsuario = True
    else:
        TUsuario = False

    nombres_productos = []    #Aqui se crea un lista para pasar los productos comprados
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            producto = Producto.objects.get(id=value["producto_id"])
            nombres_productos.append(producto.nombre)

    productosComprados = ", ".join(nombres_productos)

    data = { #Datos enviados para mostrar al finalizar compra
        'estado' : estado,
        'fecha' : fecha,
        'monto' : resp.get('amount'),
        'Ncuotas' : resp.get('installments_number'),
        'tarjeta' :  resp.get('card_detail').get('card_number'),
        'comprobante' :  resp.get('authorization_code'),
        'ordenCompra' : resp.get('buy_order'),
        'productos' : productosComprados
    }

    if estado == 'FAILED':
        return redirect('pagoFallido')
    
    else:
        newHistorial = Historial(
            email = resp.get('session_id'),
            fecha = fecha,
            total = resp.get('amount'),
            tipoPago = False,
            tipoUsuario = TUsuario,
        )
        newHistorial.save()
            
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            newDetalle = DetalleCompra(
                idHistorial = newHistorial.id,
                idProducto = value["producto_id"],
                cantidad = value["cantidad"]
            )
            newDetalle.save()
        for key, value in request.session["carrito"].items():
            carrito = Carrito(request)
            carrito.limpiar()
        
        if TUsuario == False:
            del request.session['email']
            request.session.modified = True
        
        return render(request, 'core/pagoExitoso.html', data)

def recorrer_productos(request):
    nombres_productos = []    #Aqui se crea un lista para pasar los productos comprados
    if 'carrito' in request.session:
        for key, value in request.session["carrito"].items():
            producto = Producto.objects.get(id=value["producto_id"])
            nombres_productos.append(producto.nombre)

    productosComprados = ", ".join(nombres_productos)
    return productosComprados


def RetornoTransaccion2(request):
    token_ws = request.GET.get('token_ws')  # Obtener el token de la transacción desde la URL
    if not token_ws:
        return redirect('pagoFallido') 
    transaction = Transaction()
    resp = transaction.commit(token_ws)

    estado = resp.get('status')
    fechaISO8601 = resp.get('transaction_date')
    fecha_hora = datetime.strptime(fechaISO8601, '%Y-%m-%dT%H:%M:%S.%fZ') # Analiza la fecha
    fecha = fecha_hora.strftime('%d-%m-%Y %H:%M:%S') #Seteo del nuevo formato
    
    # try:
    #     tipoUsuario = request.session['tipoUsuario'] #para error
    # except KeyError:
    #     tipoUsuario = 0

   
    # if tipoUsuario <= 0:
    #     TUsuario = True
    # else:
    #     TUsuario = False
    productos_carrito = recorrer_productos(request)

    data = { #Datos enviados para mostrar al finalizar compra
        'estado' : estado,
        'fecha' : fecha,
        'monto' : resp.get('amount'),
        'Ncuotas' : resp.get('installments_number'),
        'tarjeta' :  resp.get('card_detail').get('card_number'),
        'comprobante' :  resp.get('authorization_code'),
        'ordenCompra' : resp.get('buy_order'),
        'productos' : productos_carrito
    }

    if estado == 'FAILED':
        return redirect('pagoFallido')
    
    else:
        newHistorial = Historial(
            email = resp.get('session_id'),
            fecha = fecha,
            total = resp.get('amount'),
            tipoPago = False,
            tipoUsuario = True, #momentaneo
        )
        newHistorial.save()
            
        # for key, value in request.session["carrito"].items():
        #     carrito = Carrito(request)
        #     newDetalle = DetalleCompra(
        #         idHistorial = newHistorial.id,
        #         idProducto = value["producto_id"],
        #         cantidad = value["cantidad"]
        #     )
        #     newDetalle.save()
        # for key, value in request.session["carrito"].items():
        #     carrito = Carrito(request)
        #     carrito.limpiar()
        
        # if TUsuario == False:
        #     del request.session['email']
        #     request.session.modified = True
        
        return render(request, 'core/pagoExitoso.html', data)
    
def pagoExitoso(request):
    return render(request, 'core/pagoExitoso.html')

def pagoFallido(request):
    return render(request, 'core/pagoFallido.html')

class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
