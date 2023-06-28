function crearCuadroProducto(imagen, nombre, precio, descripcion) {
    var cuadro = `
        <div class="item">
            <figure>
                <img style="width: 120px"
                src="${imagen}"
                alt="${nombre}"
                />
            </figure>
            <h3>${nombre}</h3>
            <p>${descripcion}</p>
            <p>Precio: ${precio}</p>
        </div>
    `;
    return cuadro;
}

$(document).ready(function (event) {

    let url = "https://fakestoreapi.com/products";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // para limpiar el contedor antes de desplegar
            $("#ropa").empty();

            $.each(data, function(i, item) {
                var cuadro = crearCuadroProducto(item.image, item.title, item.price, item.description);
                $('#ropa').append(cuadro);
            });
        });
});
