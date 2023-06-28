from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):

    id_perfil = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="images/")
    rut = models.PositiveIntegerField(unique=True)
    dv = models.CharField(max_length=1)
    subscrito = models.BooleanField(default=False)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
