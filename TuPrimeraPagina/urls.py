# TuPrimeraPagina/urls.py

from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # 1. URL del Panel de Administración
    path('admin/', admin.site.urls),
    
    # 2. URL de tu Aplicación Blog (Ruta principal)
    path('', include('blog.urls')),
    
    # 3. 🔑 URLs de Autenticación de Django (Login, Logout, Password Reset)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 4. 💬 URL de tu Aplicación Mensajería (Ruta nueva)
    path('mensajeria/', include('mensajes.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)