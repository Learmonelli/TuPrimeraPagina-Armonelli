from django.contrib import admin
# Necesario importar 'include'
from django.urls import path, include 

urlpatterns = [
    # 1. URL del Panel de Administración
    path('admin/', admin.site.urls),
    
    # 2. URL de tu Aplicación Blog
    # La ruta vacía '' significa que las URLs de 'blog' se atienden desde la raíz del sitio.
    path('', include('blog.urls')),
    
    # 3. 🔑 URLs de Autenticación de Django (Soluciona el error 'NoReverseMatch' de 'login')
    # Esto agrega automáticamente 'login', 'logout', 'password_change', etc., bajo el prefijo 'accounts/'.
    path('accounts/', include('django.contrib.auth.urls')), 
]