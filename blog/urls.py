from django.urls import path
from . import views

urlpatterns = [
    # Vistas generales
    path('', views.inicio, name='Inicio'),

    # Vistas de Creación
    path('autor/crear/', views.crear_autor, name='CrearAutor'),
    path('categoria/crear/', views.crear_categoria, name='CrearCategoria'),
    path('post/crear/', views.crear_post, name='CrearPost'),

    # Vistas de Búsqueda
    path('post/buscar/', views.buscar_post, name='BuscarPost'),
]