
//  onclick="enviar_correo()"
// function enviar_correo() {
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/enviar_correo');
//     console.log("Hola Mundo");
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.onload = function() {
//         if (xhr.status === 200) {
//             alert('El correo electrónico se ha enviado correctamente.');
//         } else {
//             alert('Ha ocurrido un error al enviar el correo electrónico.');
//         }
//     };
//     console.log("Hola Mundo");
//     xhr.send(JSON.stringify({
        
//         'destinatario': 'alva.jara@duocuc.cl',
//         'asunto': 'Prueba de venta',
//         'cuerpo': 'Este es un correo electrónico enviado desde JavaScript y HTML. CHETAO CHETAO CHETAO CHETAO'
//     }));
//     console.log("Hola Mundo");
// }