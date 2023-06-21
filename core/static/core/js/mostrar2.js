var myButton = document.getElementById("btn-opcion");
var myOption = document.getElementById("myOption");
var myOption1 = document.getElementById("Formcliente");
var rut = document.getElementById("rut");
var telefono = document.getElementById("telefono");
myButton.addEventListener("click", function(){
if (rut.value === '') {

}else{
    if (telefono.value === '') {
    
    }else{
        if (myOption.style.display === "none") {
            myOption.style.display = "block";
            myOption1.style.display = "none";
        } else {
            myOption.style.display = "none";
        }
    }
} 
});

var atrasEnvio = document.getElementById("atrasEnvio");
atrasEnvio.addEventListener("click", function(){
    if (myOption.style.display === "block") {
        myOption.style.display = "none";
        myOption1.style.display = "block";
        myOption2.style.display = "none";
    } else {
        myOption.style.display = "block";
    }
});

var myButton2 = document.getElementById("btn-opcion2");
var myOption2 = document.getElementById("myOption2");
var direccion = document.getElementById("direccion");
var ciudad = document.getElementById("ciudad");
var estado = document.getElementById("estado");
var codigo_postal = document.getElementById("codigo_postal");
myButton2.addEventListener("click", function(){
if (direccion.value === '') {

}else{
    if (ciudad.value === '') {
        
    }else{
        if (estado.value === '' ) {

        }else{
            if (codigo_postal.value === '' ) {

                }else{  
                    if (myOption2.style.display === "none") {
                        myOption2.style.display = "block";
                    } else {
                        myOption2.style.display = "none";
                    }
            }
        }
    }
    
    
    
}
});

var pagar = document.getElementById("pagar");
var metodoPago = document.getElementById("metodoPago");
pagar.addEventListener("click", function(){
if (metodoPago.value === 'None') {
    event.preventDefault();
    alert('Debes seleccionar una opcion');
    setError(form.metodoPago, 'Debe escoger un metodo de pago')
}else{
    
}
});

// function transfer (){
//     var valorActivo = document.querySelector('input[name="MetodPago"]:checked').value;
//     var datos = document.getElementById("datosTransferencia");
//     if (valorActivo === "transferencia") {
//         comprar.href = "{% url 'datoTransferencia' %}";
//     } else {
//         comprar.href = "{% url  'comprar' %}";

//     }
// }


var valorActivo = document.getElementById("miRadio1");
var comprar = document.getElementById('comprar');
comprar.addEventListener('click', function() {
    comprar.href = "{% url 'datoTransferencia' %}";
    console.log(valorActivo)
});


// $(document).ready(function () {

//     var userAgent = navigator.userAgent
  
//     if (userAgent.match(/Windows/i)) {
//       $("#codigoQR").append("<h3 class='text-light' id='DescargaAqui' >Descarga aquí</h3>");
//       $("#codigoQR").append("<img src='static/core/img/flecha_down.png' alt='qr' id='flecha_down'></img>");
//       $("#codigoQR").append("<img src='static/core/img/qrAPK.png' alt='qr' id='QR'></img>");
//     } else {
//       $("#codigoQR").append("<h3 class='text-light' id='DescargaAqui' >Descarga aquí</h3>");
//       $("#codigoQR").append("<img src='static/core/img/flecha_down.png' alt='qr' id='flecha_down'></img>");
//       $("#codigoQR").append('<a href="static/core/apk/DuocQR.apk"  id="botonDescarga" class="btn">DESCARGAR</a>');
//     }
  
//   });
