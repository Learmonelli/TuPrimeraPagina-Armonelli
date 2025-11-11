from django.urls import path
from . import views

urlpatterns = [
    # 1. Vistas Generales
    path('', views.inicio, name='inicio'),

    # 2. Vistas de Creación/Manipulación (CRUD - Create/Update/Delete)
    path('autor/crear/', views.crear_autor, name='crear_autor'),       
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'), 
    path('post/crear/', views.crear_post, name='crear_post'),
    
    # 🔑 RUTA REQUERIDA: Edición de Post
    path('post/editar/<int:pk>/', views.editar_post, name='editar_post'), 
    
    path('post/eliminar/<int:pk>/', views.eliminar_post, name='eliminar_post'), 

    # 3. Vistas de Búsqueda
    path('post/buscar/', views.buscar_post, name='buscar_post'),     

    # 4. Vistas de Autenticación y Perfil
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editarPerfil, name='editarPerfil'), 
    path('avatar/agregar/', views.agregarAvatar, name='agregar_avatar'),
    path('about/', views.about, name='about'),

    # Vista de Detalle
    path('pages/<int:pk>/', views.detalle_post, name='detalle_post'), 
]