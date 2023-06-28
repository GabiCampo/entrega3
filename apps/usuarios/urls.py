from django.urls import path
from . import views

urlsUsuarios = [
    path("registro", views.registrarse, name="registro"),
    path("login", views.iniciar_sesion, name="iniciarsesion"),
    path("logout", views.cerrar_sesion, name="cerrarsesion")
]

urlsPrincipal = [
    path("", views.paginaInicio, name="paginainicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("misdatos/<str:username>", views.mis_datos, name="misdatos")
]