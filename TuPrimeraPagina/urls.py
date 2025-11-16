# miprimerpagina/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Para MEDIA
from django.conf.urls.static import static # Para MEDIA

urlpatterns = [
    # 1. ADMIN
    path('admin/', admin.site.urls),
    
    # 2. APP BLOG (Página de inicio del sitio es el blog)
    # Si dejas la ruta vacía, la página de inicio será la de blog.urls
    path('', include('blog.urls')), 
    
    # 3. APP ACCOUNTS (Autenticación y Perfil)
    # Agrupamos todas las URLs de accounts bajo 'accounts/'
    path('accounts/', include('accounts.urls')),
    
    # 4. URLs de Autenticación por defecto de Django
    # Incluye login, logout, password_change, etc. 
    # Usamos 'django.contrib.auth.urls' para obtener:
    # - accounts/login/ (name='login')
    # - accounts/logout/ (name='logout')
    # - accounts/password_change/ (name='password_change')
    # - etc.
    # Por defecto, Django Auth busca los templates en 'registration/' o 'accounts/registration/'
    path('accounts/', include('django.contrib.auth.urls')),
    path('mensajes/', include('mensajes.urls')),
]

# Configuración de Archivos MEDIA (¡Necesario para Avatars e imágenes de Posts!)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)