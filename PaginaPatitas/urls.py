from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.usuarios.urls import urlsUsuarios, urlsPrincipal
from apps.producto.urls import urlsProducto, urlsBoletas
from apps.administracion.urls import urlsAdministracion

urlpatterns = [
    path('admin/', admin.site.urls),
    path("paginainicio/", include(urlsPrincipal)),
    path("usuarios/", include(urlsUsuarios)),
    path("administracion/", include(urlsAdministracion)),
    path("productos/", include(urlsProducto)),
    path("boleta/", include(urlsBoletas))
] 


# Ruta para servir archivos de medios (imágenes)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


