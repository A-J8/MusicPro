function generarinfo() {
    const doc = new jsPDF()
    console.log("funca")
    doc.autoTable({html: "#tabla"})
    doc.save("Reporte_Transacciones.pdf")
}