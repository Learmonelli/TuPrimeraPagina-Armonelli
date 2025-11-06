from django.urls import path
from . import views
# No necesitas importar 'editarPerfil' aquí si ya tienes 'from . import views'
# from .views import editarPerfil # <-- Línea Eliminada

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
    
    # URL de Registro
    path('registro/', views.registro, name='registro'), 
    
    # URL para ver el Perfil (necesaria para la redirección de edición)
    path('perfil/', views.perfil, name='perfil'),
    
    # URL para Editar el Perfil - **RECOMENDACIÓN:** Usa una URL consistente:
    path('editar-perfil/', views.editarPerfil, name='editar_perfil'), 
    
    # Si quieres mantener tu URL antigua por un tiempo, puedes añadirla como alias:
    # path('editarPerfil/', views.editarPerfil, name='EditarPerfil'), 
]