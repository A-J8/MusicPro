function generarinfo() {
    const doc = new jsPDF()
    console.log("funca")
    doc.autoTable({html: "#tabla"})
    doc.save("Reporte_Transacciones.pdf")
}


// function generarPDF() {
//     // Obtiene el elemento canvas del gráfico
//     var canvas = document.getElementById('container');
  
//     // Convierte el canvas a una imagen en formato PNG
//     var imagen = canvas.toDataURL('image/png');
  
//     // Crea un nuevo documento PDF
//     var doc = new jsPDF();
  
//     // Inserta la imagen del gráfico en el documento PDF
//     doc.addImage(imagen, 'PNG', 10, 10, 100, 50);
  
//     // Descarga el PDF generado
//     doc.save('grafico.pdf');
//   }


  function downloadPDF() {
    // Crea un nuevo objeto jsPDF
    const doc = new jsPDF();
  
    // Obtiene el gráfico Highcharts y crea una imagen a partir de él
    const svg = document.querySelector('#container').innerHTML;
    const canvas = document.createElement();
    canvg(canvas, svg);
    const imgData = canvas.toDataURL('image/png');
  
    // Agrega la imagen al documento PDF
    doc.addImage(imgData, 'PNG', 10, 10, 180, 100);
  
    // Descarga el archivo PDF
    doc.save('chart.pdf');
  }