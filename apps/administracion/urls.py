from django.urls import path
from . import views

urlsAdministracion = [
    path("", views.administracion, name="administrar"),
    path("bodegas/", views.bodega, name="bodega"),
    path("productos/", views.producto, name="producto"),
    path("producto/<int:id>", views.eliminarProducto, name="eliminarproducto"),
    path("producto-actualizar/<int:id>", views.actualizarProducto, name="actualizarproducto"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuario/delete/<int:id>", views.eliminar_usuario, name="eliminarusuario"),
    path("usuario/update/<int:id>", views.actualizar_usuario, name="actualizarusuario"),
    path("ventas/", views.historial_ventas, name="historial_ventas")
]