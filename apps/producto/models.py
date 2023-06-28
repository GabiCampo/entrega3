from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)


class Producto(models.Model):

    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="images/", null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    oferta = models.PositiveSmallIntegerField(default=0)

class Bodega(models.Model):
    
    id_bodega = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()


CHOICES_CONDITION = [
    ("Entregado", "Entregado"),
    ("Despachado", "Despachado"),
    ("Vendido", "Vendido"),
    ("Preparacion", "Preparacion")
]

class Boleta(models.Model):

    id_boleta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(default="", blank=True, null=True)
    monto_total = models.PositiveIntegerField()
    estado = models.CharField(max_length=40, choices=CHOICES_CONDITION)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class DetalleBoleta(models.Model):

    id_detalle_boleta = models.AutoField(primary_key=True)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)