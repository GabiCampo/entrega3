from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto, Boleta
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Perfil

# Create your views here.

def obtener_productos(request):
    categoria_id = request.GET.get('categoria_id')
    productos = Producto.objects.filter(categoria=categoria_id).values('id_producto', 'nombre')
    return JsonResponse(list(productos), safe=False)

def listar_productos(request):

    productos = Producto.objects.filter(disponible=True)

    if request.method == "GET":

        contexto = {
            "productos": productos
        }

        return render(request, "productos.html", contexto)

def obtener_producto(request, id:int):

    producto = Producto.objects.get(id_producto = id)

    if request.method == "GET":

        if producto.oferta:

            oferta = producto.oferta

            porcentaje_oferta = oferta / 100

            procentaje_precio = producto.precio * porcentaje_oferta

            precio_oferta = producto.precio - procentaje_precio
        else:
            precio_oferta = 0

        contexto = {
            "producto": producto,
            "precio_oferta": int(precio_oferta)
        }

        return render(request, "producto_1.html", contexto)

@login_required
def mostrar_datos_boleta(request, id_usuario:int):

    mis_compras = Boleta.objects.filter(usuario=id_usuario)

    if len(mis_compras):
        contexto = {
            "compras": mis_compras
        }
    else:
        contexto = {
            "message": "No tiene ninguna compra registrada"
        }

    return render(request, "mis_compras.html", contexto)

@login_required
def detalle_boleta(request, id_boleta:int):

    boleta = Boleta.objects.get(id_boleta = id_boleta)


    if request.method == "GET":

        cliente = Perfil.objects.get(id_usuario = boleta.usuario)

        subscrito = 0

        if cliente.subscrito:
            subscrito = 5

        oferta_producto = boleta.producto.oferta

        descuento_total = oferta_producto + subscrito

        decimal_descuento = descuento_total / 100

        precio_descuento = boleta.monto_total * decimal_descuento

        iva = 0.19

        precio_iva = int(boleta.monto_total * iva)

        precio_con_iva = boleta.monto_total + precio_iva

        contexto = {
            "boleta": boleta,
            "cliente": cliente,
            "descuento_total": descuento_total,
            "precio_descuento": int(precio_descuento),
            "precio_iva": precio_iva,
            "precio_con_iva": precio_con_iva
        }

        return render(request, "boleta_detalle.html", contexto)

def concurso_ropa(request):

    return render(request, "concurso_ropa.html")