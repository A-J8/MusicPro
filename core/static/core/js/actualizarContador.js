    btnPagos.addEventListener("click", function(){
    if (tblPagos.style.display === "none") {
        tblPagos.style.display = "block";
        tblEnvios.style.display = "none";
    } else {
        tblPagos.style.display = "none";
    }
    });

    btnEnvios.addEventListener("click", function(){
    if (tblEnvios.style.display === "none") {
        tblEnvios.style.display = "block";
        tblPagos.style.display = "none";
    } else {
        tblEnvios.style.display = "none";
    }
    });

    btnInicio.addEventListener("click", function(){
    tblPagos.style.display = "none";
    tblEnvios.style.display = "none";
    
    });

function cambiarEstado(boton) {
    var estado = boton.parentNode.previousElementSibling;
    if (estado.classList.contains("true")) {
        estado.classList.remove("true");
        estado.classList.add("false");
        estado.textContent = "Procesando";
    } else {
        estado.classList.remove("false");
        estado.classList.add("true");
        estado.textContent = "Aprobado";
    }
}