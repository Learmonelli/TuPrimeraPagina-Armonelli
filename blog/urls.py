from django.urls import path
from . import views

urlpatterns = [
    # ==================================
    # 1. Vistas Generales
    # ==================================
    path('', views.inicio, name='Inicio'),

    # ==================================
    # 2. Vistas de Creación (CRUD - Create)
    # ==================================
    path('autor/crear/', views.crear_autor, name='CrearAutor'),
    path('categoria/crear/', views.crear_categoria, name='CrearCategoria'),
    path('post/crear/', views.crear_post, name='CrearPost'),

    # ==================================
    # 3. Vistas de Búsqueda
    # ==================================
    path('post/buscar/', views.buscar_post, name='BuscarPost'),

    # ==================================
    # 4. Vistas de Autenticación y Perfil
    # ==================================
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editarPerfil, name='editar_perfil'),
    path('avatar/agregar/', views.agregarAvatar, name='agregar_avatar'), # Ruta de Avatar
    
    # Si quieres mantener el alias antiguo por compatibilidad:
    # path('editarPerfil/', views.editarPerfil, name='EditarPerfil'), 

]
