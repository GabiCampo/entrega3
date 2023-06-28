from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.producto.models import Producto, Categoria, Bodega, Boleta
from apps.usuarios.models import Perfil
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
@login_required
def administracion(request):
    return render(request, 'administrar.html')

@login_required
def bodega(request):
# solo admin
    categorias = Categoria.objects.all()
    bodegas = Bodega.objects.all()

    if request.method == "GET":

        contexto = {
            "categorias": categorias,
            "bodegas": bodegas
        }

        return render(request, 'bodega.html', contexto)

    elif request.method == "POST":

        categoria = request.POST["categoria"]
        producto = request.POST["producto"]
        cantidad = request.POST["cantidad"]

        try:

            categoriaEncontrada = Categoria.objects.get(id_categoria=categoria)

        except ValueError:
            contexto = {
                'mensage4': 'Tiene que seleccionar una categoria',
                'categorias': categorias
            }
            return render(request, 'bodega.html', contexto)

        try:

            productoEncontrado = Producto.objects.get(id_producto=producto)

        except ValueError:
            contexto = {
                'mensage4': 'Tiene que seleccionar un producto',
                'categorias': categorias
            }
            return render(request, 'bodega.html', contexto)

        nuevaBodega = Bodega()

        nuevaBodega.categoria = categoriaEncontrada
        nuevaBodega.producto = productoEncontrado
        nuevaBodega.cantidad = cantidad

        nuevaBodega.save()

        return HttpResponseRedirect(reverse("administrar"))

@login_required
def producto(request):

    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponible=True)

    if request.method == "GET":

        contexto = {
            "categorias": categorias,
            "productos": productos
        }

        return render(request, "admin_productos.html", contexto)

    elif request.method == "POST":

        id_producto = request.POST["id_producto"]
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripcion"]
        imagen = request.FILES["imagen"]
        categoria = request.POST["categorias"]
        oferta = request.POST["oferta"]

        try:
            categoriaEncontrada = Categoria.objects.get(id_categoria = categoria)
        except Categoria.DoesNotExist:
            return render(request, "admin_productos.html")

        producto = Producto()

        producto.id_producto = id_producto
        producto.nombre = nombre
        producto.precio = precio
        producto.descripcion = descripcion
        producto.imagen = imagen
        producto.oferta = oferta
        producto.categoria = categoriaEncontrada

        producto.save()

        return HttpResponseRedirect(reverse("administrar"))

@login_required
def eliminarProducto(request, id:int):

    producto = Producto.objects.get(id_producto=id)

    if request.method == "GET":

        producto.delete()

        return HttpResponseRedirect(reverse("producto"))

@login_required
def actualizarProducto(request, id:int):

    producto = Producto.objects.get(id_producto=id)
    categorias = Categoria.objects.all()

    if request.method == "GET":

        contexto = {
            "producto": producto,
            "categorias": categorias
        }

        return render(request, "actualizar_producto.html", contexto)
    
    elif request.method == "POST":

        id_producto = request.POST["id_producto"]
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripcion"]
        categoria = request.POST["categorias"]
        oferta = request.POST["oferta"]

        try:
            categoriaEncontrada = Categoria.objects.get(id_categoria = categoria)
        except Categoria.DoesNotExist:
            return render(request, "admin_productos.html")

        try:
            imagen = request.FILES['imagen']
        except MultiValueDictKeyError:
            imagen = producto.imagen

        producto.id_producto = id_producto
        producto.nombre = nombre
        producto.precio = precio
        producto.descripcion = descripcion
        producto.imagen = imagen
        producto.oferta = oferta
        producto.categoria = categoriaEncontrada

        producto.save()

        return HttpResponseRedirect(reverse("producto"))

@login_required
def usuarios(request):

    usuarios = User.objects.all()
    perfiles = Perfil.objects.select_related('id_usuario').all()

    if request.method == "GET":

        contexto = {
            "usuarios": usuarios,
            "perfiles": perfiles
        }

        return render(request, "admin_usuarios.html", contexto)

    elif request.method == "POST":

        id_usuario = request.POST["id_usuario"]
        rol = request.POST["rol"]
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido =request.POST["apellido"]
        correo = request.POST["correo"]
        direccion = request.POST["direccion"]
        subscripcion = request.POST.get("subscripcion")
        contrasena = request.POST["contrasena"]

        try:
            imagen = request.FILES['imagen']
        except MultiValueDictKeyError:
            imagen = producto.imagen

        username = nombre + "." + apellido

        rut_dividido = rut.split("-")

        if rol == "0":
            superuser = False

        elif rol == "1":
            superuser = True

        if subscripcion == "1":
            subscripcion_bool = True
        else:
            subscripcion_bool = False

        nuevo_usuario = User.objects.create(
                    id = id_usuario,
                    first_name = nombre,
                    last_name = apellido,
                    username = username,
                    email = correo,
                    is_superuser = superuser,
                    password = contrasena
                )
        nuevo_usuario.set_password(contrasena)

        nuevo_perfil = Perfil()
        nuevo_perfil.id_usuario = nuevo_usuario
        nuevo_perfil.direccion = direccion
        nuevo_perfil.subscrito = subscripcion_bool
        nuevo_perfil.rut = rut_dividido[0]
        nuevo_perfil.dv = rut_dividido[1]
        nuevo_perfil.imagen = imagen

        nuevo_usuario.save()
        nuevo_perfil.save()

        return HttpResponseRedirect(reverse("administrar"))

@login_required
def eliminar_usuario(request, id:int):

    if request.method == "GET":

        usuario = User.objects.get(id=id)
        usuario.delete()

        return HttpResponseRedirect(reverse("usuarios"))

@login_required
def actualizar_usuario(request, id:int):

    usuario_encontrado = User.objects.get(id=id)
    perfil_encontrado = Perfil.objects.get(id_usuario=usuario_encontrado)

    if request.method == "GET":

        contexto = {
            "usuario": usuario_encontrado,
            "perfil": perfil_encontrado
        }

        return render(request, "actualizar_usuario.html", contexto)

    elif request.method == "POST":

        id_usuario = request.POST["id_usuario"]
        rol = request.POST["rol"]
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellido =request.POST["apellido"]
        correo = request.POST["correo"]
        direccion = request.POST["direccion"]
        subscripcion = request.POST.get("subscripcion")
        contrasena = request.POST["contrasena"]

        try:
            imagen = request.FILES['imagen']
        except MultiValueDictKeyError:
            imagen = perfil_encontrado.imagen

        if contrasena == "":
            contrasena = usuario_encontrado.password

        username = nombre + "." + apellido

        rut_dividido = rut.split("-")

        if rol == "0":
            superuser = False

        elif rol == "1":
            superuser = True

        if subscripcion == "1":
            subscripcion_bool = True
        else:
            subscripcion_bool = False

        usuario_encontrado.set_password(contrasena)

        usuario_encontrado.id = id_usuario
        usuario_encontrado.first_name = nombre
        usuario_encontrado.last_name = apellido
        usuario_encontrado.username = username
        usuario_encontrado.is_superuser = superuser
        usuario_encontrado.email = correo
        usuario_encontrado.password = contrasena

        perfil_encontrado.direccion = direccion
        perfil_encontrado.subscrito = subscripcion_bool
        perfil_encontrado.rut = rut_dividido[0]
        perfil_encontrado.dv = rut_dividido[1]
        perfil_encontrado.imagen = imagen

        usuario_encontrado.save()
        perfil_encontrado.save()

        return HttpResponseRedirect(reverse("usuarios"))

@login_required
def historial_ventas(request):

    if request.method == "GET":

        ventas = Boleta.objects.all()

        contexto = {
            "ventas": ventas
        }

        return render(request, "historial_venta.html", contexto)