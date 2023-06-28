from django.contrib import admin
from .models import Producto, Categoria, Boleta

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria','nombre']
    list_filter = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_producto','nombre', 'precio', 'disponible']
    list_filter = ('nombre', 'disponible')
    exclude = ('id_oferta',)

@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ['fecha_venta', 'fecha_entrega', 'monto_total', 'estado', 'usuario', 'producto']
    list_filter = ('usuario', 'producto')
    exclude = ('fecha_venta',)