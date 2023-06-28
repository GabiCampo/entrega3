from django.urls import path
from . import views

urlsProducto = [
    path("categoria/", views.obtener_productos, name="obtener_productos"),
    path("", views.listar_productos, name="productos"),
    path("producto/<int:id>", views.obtener_producto, name="producto"),
    path("concurso-ropa/", views.concurso_ropa, name="concurso_ropa")
]

urlsBoletas = [
    path("usuario/<int:id_usuario>", views.mostrar_datos_boleta, name="mis_compras"),
    path("detalle/<int:id_boleta>", views.detalle_boleta, name="detalle_boleta")
]