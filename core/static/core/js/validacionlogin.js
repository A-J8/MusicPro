$(document).ready(function(){
    $("#CorreoUSUARIO").on("input", function () {
        if ($("#CorreoUSUARIO").val() == "") {
            $("#CorreoUSUARIO").addClass("error");
            $("#CorreoUSUARIO").removeClass("ok");
            $("#mensaje3").html("¡Ingrese un Correo Electrónico!");
        }
        else {
            if ($("#CorreoUSUARIO").val().indexOf("@")>=0){
                $("#CorreoUSUARIO").removeClass("error");
                $("#CorreoUSUARIO").addClass("ok");
                $("#mensaje3").html("✓ ")
            }else{
                $("#CorreoUSUARIO").addClass("error");
                $("#CorreoUSUARIO").removeClass("ok");
                $("#mensaje3").html("¡Ingrese un Correo Electrónico!");
            }
        }
    })

    $("#CorreoADMIN").on("input", function () {
        if ($("#CorreoADMIN").val() == "") {
            $("#CorreoADMIN").addClass("error");
            $("#CorreoADMIN").removeClass("ok");
            $("#mensaje3").html("¡Ingrese un Correo Electrónico!");
        }
        else {
            if ($("#CorreoADMIN").val().indexOf("@")>=0){
                $("#CorreoADMIN").removeClass("error");
                $("#CorreoADMIN").addClass("ok");
                $("#mensaje3").html("✓ ")
            }else{
                $("#CorreoADMIN").addClass("error");
                $("#CorreoADMIN").removeClass("ok");
                $("#mensaje3").html("¡Ingrese un Correo Electrónico!");
            }
        }
    })
    

    $("#ClaveUSUARIO").on("input", function(){
      if ($("#ClaveUSUARIO").val() == ""){   
        $("#ClaveUSUARIO").addClass("error");
        $("#ClaveUSUARIO").removeClass("ok");
        event.preventDefault();
      }else{
        $("#ClaveUSUARIO").removeClass("error");
        $("#ClaveUSUARIO").addClass("ok");
      }
    })

    $("#ClaveADMIN").on("input", function(){
      if ($("#ClaveADMIN").val() == ""){
        $("#ClaveADMIN").addClass("error");
        $("#ClaveADMIN").removeClass("ok");
        event.preventDefault();
        alert("Complete el campo de la contraseña");
      }else{
        $("#ClaveADMIN").removeClass("error");
        $("#ClaveADMIN").addClass("ok");
      }

    })

    $("#btnIniciarSesionUSUARIO").click(function(){
        if ($("#CorreoUSUARIO").val() == "" || $("#ClaveUSUARIO").val() == ""){
            $("#CorreoUSUARIO").addClass("error");
            $("#CorreoUSUARIO").removeClass("ok");
            $("#ClaveUSUARIO").addClass("error");
            $("#ClaveUSUARIO").removeClass("ok");       
            event.preventDefault();
            alert("Complete los campos vacíos");
        }

        if($("#CorreoUSUARIO").val().indexof("@") >= 0){
            $("#CorreoUSUARIO").addClass("ok");
            $("#CorreoUSUARIO").removeClass("error");

            
        }else{
            $("#CorreoUSUARIO").addClass("error");
            $("#CorreoUSUARIO").removeClass("ok");
            event.preventDefault();
        }
        

    })

    $("#btnIniciarSesionADMIN").click(function(){
        if ($("#CorreoADMIN").val() == "" || $("#ClaveADMIN").val() == "" ){
            $("#CorreoADMIN").addClass("error");
            $("#CorreoADMIN").removeClass("ok");
            $("#ClaveADMIN").addClass("error");
            $("#ClaveADMIN").removeClass("ok");     
            event.preventDefault();
            alert("Complete los campos vacíos");
        }

        if($("#CorreoADMIN").val().indexof("@") >= 0){
            $("#CorreoADMIN").addClass("ok");
            $("#CorreoADMIN").removeClass("error");
            
        }else{
            $("#CorreoADMIN").addClass("error");
            $("#CorreoADMIN").removeClass("ok");
            event.preventDefault();
        }
    

        
    })




})