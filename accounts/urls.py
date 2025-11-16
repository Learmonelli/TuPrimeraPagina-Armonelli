from django.urls import path
from . import views

urlpatterns = [
    # 📝 Registro
    path('registro/', views.registro, name='registro'),

    # 🔑 Perfil de Usuario
    path('perfil/', views.perfil, name='perfil'),
    
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'), 
    
    # 🖼️ Avatar
    # 🛑 CORREGIDO: De views.agregar_avatar a views.agregarAvatar
    path('agregar_avatar/', views.agregarAvatar, name='agregar_avatar'), 
]