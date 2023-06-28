from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Perfil
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

def paginaInicio(request):
    return render(request, "inicio.html")

def registrarse(request):

    if request.method == "GET":
        return render(request, "Registro.html")

    elif request.method == "POST":

        rut = request.POST["txtRut"]
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        usuario = request.POST["txtUsuario"]
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        subscripcion = request.POST.get("chSubscripcion")
        contrasena = request.POST["txtContrasena"]
        confirmar_contrasena = request.POST["txtRepetirContrasena"]
        imagen = request.FILES["txtimagen"]
        
        rut_dividido = rut.split("-") # Para poder dividir el rut del usuario

        if contrasena == confirmar_contrasena:

            try:

                usuario_creado, nuevo_usuario = User.objects.get_or_create(
                    first_name = nombre,
                    last_name = apellido,
                    username = usuario,
                    email = email,
                    password = contrasena
                )

            except IntegrityError:
                contexto = {}
                contexto['mensage']= 'Usuario ya existe *'
                return render(request, 'Registro.html', contexto)
        else:
            contexto = {}
            contexto['mensage_contrasena']= 'Contraseñas invalidas *'
            return render(request, 'Registro.html', contexto)

        if subscripcion == "1":
            subscripcion = True
        else:
            subscripcion = False

        if nuevo_usuario:
            usuario_creado.set_password(contrasena)
            usuario_creado.save()
            nuevoPerfil = Perfil()
            nuevoPerfil.id_usuario = usuario_creado
            nuevoPerfil.rut = rut_dividido[0]
            nuevoPerfil.dv = rut_dividido[1]
            nuevoPerfil.direccion = direccion
            nuevoPerfil.imagen = imagen
            nuevoPerfil.subscrito = subscripcion
            nuevoPerfil.save()

        return HttpResponseRedirect(reverse('paginainicio'))

def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "inicio_sesion.html")

    elif request.method == "POST":

        email = request.POST["txtEmail"]
        contrasena = request.POST["txtContrasena"]
        user = User.objects.filter(email=email).first()
        # Autenticar al usuario
        userEncontrado = authenticate(username=user.username, password=contrasena)

        if userEncontrado is not None:
            # El usuario ha sido autenticado correctamente
            login(request, userEncontrado)
            return HttpResponseRedirect(reverse('paginainicio'))
        else:
            # Las credenciales son incorrectas
            contexto = {}
            contexto['mensaje'] = 'Credenciales invalidas'
            return render(request, 'inicio_sesion.html', contexto)
    

@login_required
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('paginainicio'))


def nosotros(request):
    return render(request, "nosotros.html")

@login_required
def mis_datos(request, username:str):

    usuario = User.objects.get(username=username)
    perfil = Perfil.objects.get(id_usuario = usuario)

    if request.method == "GET":

        contexto = {
            "usuario": usuario,
            "perfil": perfil
        }

        return render(request, "misdatos.html", contexto)

    elif request.method == "POST":

        rut = request.POST["txtRut"]
        nombre = request.POST["txtNombre"]
        apellido =request.POST["txtApellido"]
        correo = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        subscripcion = request.POST.get("subscripcion")
        contrasena = request.POST["txtContrasena"]

        try:
            imagen = request.FILES['subidaimagenes']
        except MultiValueDictKeyError:
            imagen = perfil.imagen

        rut_dividido = rut.split("-")

        if contrasena == "":
            contrasena = usuario.password

        if subscripcion == "1":
            subscripcion_bool = True
        else:
            subscripcion_bool = False

        usuario.set_password(contrasena)

        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.password = contrasena

        perfil.direccion = direccion
        perfil.subscrito = subscripcion_bool
        perfil.rut = rut_dividido[0]
        perfil.dv = rut_dividido[1]
        perfil.imagen = imagen

        usuario.save()
        perfil.save()
        
        return HttpResponseRedirect(reverse("paginainicio"))