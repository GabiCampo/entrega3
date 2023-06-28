// Variables
var carrito = [];
var num = 3.14159;
var numRedondeado = parseFloat(num.toFixed(2)); // 3.14

// Funciones
function agregarAlCarrito(id, nombre, precio) {
  // Buscar el producto en el carrito
  var encontrado = false;
  for (var i = 0; i < carrito.length; i++) {
    if (carrito[i].id == id) {
      carrito[i].cantidad++;
      encontrado = true;
      break;
    }
  }

  // Si no se encontró el producto, agregarlo al carrito
  if (!encontrado) {
    carrito.push({
      id: id,
      nombre: nombre,
      precio: precio,
      cantidad: 1
    });
  }

  // Actualizar el carrito y el total
  actualizarCarrito();
  actualizarTotal();
}

function actualizarCarrito() {
  // Obtener el elemento UL del carrito
  var listaCarrito = document.getElementById("lista-carrito");

  // Vaciar la lista
  listaCarrito.innerHTML = "";

  // Agregar cada producto al carrito
  for (var i = 0; i < carrito.length; i++) {
    var producto = carrito[i];

    // Crear un elemento LI para el producto
    var elemento = document.createElement("li");
    elemento.innerText = producto.nombre + " x " + producto.cantidad;
    listaCarrito.appendChild(elemento);
  }
}

function actualizarTotal() {
  // Obtener el elemento SPAN del total
  var total = document.getElementById("total");

  // Calcular el total
  var subtotal = 0;
  for (var i = 0; i < carrito.length; i++) {
    subtotal += carrito[i].precio * carrito[i].cantidad;
  }

  // Actualizar el elemento SPAN del total
  total.innerText = subtotal.toFixed(2);
}

function vaciarCarrito() {
  // Vaciar el carrito
  carrito = [];

  // Actualizar el carrito y el total
  actualizarCarrito();
  actualizarTotal();
}

// Agregar eventos de clic a los botones
var botonesAgregar = document.querySelectorAll(".agregar-carrito");
botonesAgregar.forEach(function(boton) {
  boton.addEventListener("click", function(evento) {
    var id = evento.target.dataset.id;
    var nombre = evento.target.parentNode.querySelector("h3").innerText;
    var precio = evento.target.parentNode.querySelector("p").innerText;
    precio = parseFloat(precio.replace("$", ""));
    agregarAlCarrito(id, nombre, precio);
  });
});

var botonVaciar = document.getElementById("vaciar-carrito");
botonVaciar.addEventListener("click", function() {
  vaciarCarrito();
});


