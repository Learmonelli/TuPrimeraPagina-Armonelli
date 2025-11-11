# mensajeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Muestra los mensajes recibidos por el usuario logueado (ListView)
    path('bandeja/', views.MensajeListView.as_view(), name='bandeja_entrada'),
    
    # Permite enviar un nuevo mensaje (CreateView)
    path('enviar/', views.MensajeCreateView.as_view(), name='enviar_mensaje'),
    
    # 🔑 RUTA NUEVA: Detalle de Mensaje (DetailView)
    # Usa el pk (clave primaria) para identificar el mensaje a mostrar
    path('detalle/<int:pk>/', views.MensajeDetailView.as_view(), name='detalle_mensaje'),
]