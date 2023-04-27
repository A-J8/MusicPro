$(document).ready(function () {
    
    $("#nombre").on("input", function () {
        if ($("#nombre").val() == "") {
            $("#nombre").addClass("error");
            $("#nombre").removeClass("ok");
            $("#mensaje1").html("¡Ingrese su nombre!")
        }
        else {
            $("#nombre").removeClass("error");
            $("#nombre").addClass("ok");
            $("#mensaje1").html("✓ ")
        }
    })

    $("#apellido").on("input", function () {
        if ($("#apellido").val() == "") {
            $("#apellido").addClass("error");
            $("#apellido").removeClass("ok");
            $("#mensaje2").html("¡Ingrese su Apellido!")
        }
        else {
            $("#apellido").removeClass("error");
            $("#apellido").addClass("ok");
            $("#mensaje2").html("✓ ")
        }
    })

    $("#email").on("input", function () {
        if ($("#email").val() == "") {
            $("#email").addClass("error");
            $("#email").removeClass("ok");
            $("#mensaje3").html("¡Ingrese un Correo Electrónico!")
        }
        else {
            if ($("#email").val().indexOf("@")>=0){
                $("#email").removeClass("error");
                $("#email").addClass("ok");
                $("#mensaje3").html("✓ ")
            }else{
                $("#email").addClass("error");
                $("#email").removeClass("ok");
                $("#mensaje3").html("¡Ingrese un Correo Electrónico!")
            }
        }
    })

    $("#ciudad").on("input", function () {
        if ($("#ciudad").val() == "") {
            $("#ciudad").addClass("error");
            $("#ciudad").removeClass("ok");
            $("#mensaje4").html("¡Ingrese su Ciudad!")
        }
        else {
            $("#ciudad").removeClass("error");
            $("#ciudad").addClass("ok");
            $("#mensaje4").html("✓ ")
        }
    })

    $('#submit').click(function() {
        var condiciones = $("#check").is(":checked");

        if ($("#nombre").val() == "" || $("#apellido").val() == "" || $("#email").val() == "" || $("#ciudad").val() == "" || $("#codigo").val() == ""){
            event.preventDefault();
            alert('Complete todos los campos vacios.')
    
        } else if  ($('#region').val().trim() === '') {
            event.preventDefault();
            $("#mensaje5").html("Debe seleccionar una opción.")
        }else if (!condiciones ) {
            event.preventDefault();
            $("#mensaje7").html("Acepta las condiciones.")
            
        }else{
            $("#mensaje5").html("✓ ")
        }
        
    });

    $("#codigo").on("input", function () {
        if ($("#codigo").val() == "") {
            $("#codigo").addClass("error");
            $("#codigo").removeClass("ok");
            $("#mensaje6").html("¡Ingrese el codigo postal al que pertenece!")
        }
        else {
            $("#codigo").removeClass("error");
            $("#codigo").addClass("ok");
            $("#mensaje6").html("✓ ")
        }
    })
})