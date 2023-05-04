var myButton = document.getElementById("btn-opcion");
var myOption = document.getElementById("myOption");
myButton.addEventListener("click", function(){
if (myOption.style.display === "none") {
    myOption.style.display = "block";
} else {
    myOption.style.display = "none";
}
});

var myButton2 = document.getElementById("btn-opcion2");
var myOption2 = document.getElementById("myOption2");
myButton2.addEventListener("click", function(){
    if (myOption2.style.display === "none") {
        myOption2.style.display = "block";
    } else {
        myOption2.style.display = "none";
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
