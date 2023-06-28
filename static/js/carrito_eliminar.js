// seleccionar la tabla y los elementos de los totales
var tablaProductos = document.getElementById("tabla-productos");
var subtotalElement = document.getElementById("subtotal");
var ivaElement = document.getElementById("iva");
var totalSinIvaElement = document.getElementById("total-sin-iva");
var totalAPagarElement = document.getElementById("total-a-pagar");
var num = 3.14159;
var numRedondeado = parseFloat(num.toFixed(2)); // 3.14
var botonCancelar = document.getElementById("cancelar");
var botonPagar = document.getElementById("pagar");


// agregar evento de click a los botones eliminar
tablaProductos.addEventListener("click", function(event) {
  if (event.target.classList.contains("eliminar")) {
    var fila = event.target.parentNode.parentNode;
    fila.parentNode.removeChild(fila);
    calcularTotales();
  }
});

// función para calcular los totales
function calcularTotales() {
  var subtotal = 0;
  var iva = 0;
  var totalSinIva = 0;
  var totalAPagar = 0;
  
  // recorrer todas las filas de la tabla
  var filas = tablaProductos.getElementsByTagName("tr");
  for (var i = 1; i < filas.length; i++) {
    var fila = filas[i];
    
    // obtener los valores de precio y descuentos
    var precio = parseFloat(fila.getElementsByTagName("td")[2].textContent);
    var descuentos = parseFloat(fila.getElementsByTagName("td")[6].textContent);
    
    // sumar al subtotal
    subtotal += precio - descuentos;
  }
  
  // calcular los valores de iva y totales
  iva = subtotal * 0.19;
  totalSinIva = subtotal;
  totalAPagar = subtotal + iva;
  
  // mostrar los valores en la página
  subtotalElement.textContent = subtotal.toFixed(2);
  ivaElement.textContent = iva.toFixed(2);
  totalSinIvaElement.textContent = totalSinIva.toFixed(2);
  totalAPagarElement.textContent = totalAPagar.toFixed(2);
}

// calcular los totales al cargar
calcularTotales();


botonPagar.addEventListener("click", function() {
  // Agregar aquí la lógica para procesar el pago
});

var botonCancelar = document.getElementById("cancelar");
  botonCancelar.addEventListener("click", function() {
    // Mostrar alerta al cancelar la compra
    var alerta = document.createElement("div");
    alerta.classList.add("alert");
    alerta.textContent = "Tu compra ha sido cancelada";
    document.body.appendChild(alerta);

    // Ocultar alerta después de 3 segundos
    setTimeout(function() {
      alerta.style.display = "none";
    }, 3000);
  });

