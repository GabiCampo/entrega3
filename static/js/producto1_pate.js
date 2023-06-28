var botonAgregar = document.querySelector('.agregar-carrito');
var inputPrecio = document.querySelector('.precio');
var carrito = [];
var num = 3.14159;
var numRedondeado = parseFloat(num.toFixed(2)); // 3.14

botonAgregar.addEventListener('click', function() {
  var id = botonAgregar.dataset.id;
  var nombre = botonAgregar.dataset.nombre;
  var precio = parseFloat(botonAgregar.dataset.precio);

  agregarAlCarrito(id, nombre, precio);
  actualizarCarritoUI();
});

function actualizarTotal() {
  var total = document.getElementById('total');
  var subtotal = 0;

  for (var i = 0; i < carrito.length; i++) {
    subtotal += carrito[i].precio * carrito[i].cantidad;
  }

  total.innerText = subtotal.toFixed(2);
}

