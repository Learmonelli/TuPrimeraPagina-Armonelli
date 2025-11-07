from django.contrib import admin
from django.urls import path, include 
# 🔑 Importaciones para servir archivos media en desarrollo
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # 1. URL del Panel de Administración
    path('admin/', admin.site.urls),
    
    # 2. URL de tu Aplicación Blog
    path('', include('blog.urls')),
    
    # 3. 🔑 URLs de Autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')), 
] # <-- ¡La lista urlpatterns debe cerrarse aquí!

# 🖼️ Configuración para servir archivos de medios (imágenes/avatares) en desarrollo
# ESTO DEBE IR FUERA DE LA LISTA urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)