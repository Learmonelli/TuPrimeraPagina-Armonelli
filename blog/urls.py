from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='inicio'),
    path('detalle/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.PostCrearCBV.as_view(), name='crear_post'),
    path('editar_post/<int:pk>/', views.editar_post, name='editar_post'), # ¡Añadida!
    path('eliminar_post/<int:pk>/', views.eliminar_post, name='eliminar_post'), # ¡Añadida!
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('about/', views.about, name='about'),
]