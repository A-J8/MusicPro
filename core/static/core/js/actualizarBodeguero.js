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
