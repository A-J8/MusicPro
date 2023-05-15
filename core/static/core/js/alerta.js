window.onload = function() {
    document.getElementById("DatosCliente").addEventListener("submit", function(event) {
        // Evita que el formulario se envíe de forma predeterminada
        event.preventDefault();
    
        // Muestra una alerta de SweetAlert
        swal("¡Formulario enviado!", "¡Gracias por tu compra!", "success").then(function() {
            // Una vez que se hace clic en el botón "OK" de la alerta, envía el formulario manualmente
            event.target.submit();
        });
    });
 };