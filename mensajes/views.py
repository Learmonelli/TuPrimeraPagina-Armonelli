# mensajes/views.py (COMPLETO)
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone # ⬅️ IMPORTACIÓN NECESARIA
from .models import Mensaje
from .forms import MensajeForm


# =================================================================
# 🔑 CBV 1: Listar Mensajes Recibidos (Bandeja de Entrada)
# =================================================================
class MensajeListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajes/bandeja_entrada.html'
    context_object_name = 'mensajes'
    
    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user).order_by('-fecha_envio')


# =================================================================
# 🔑 CBV 2: Enviar Mensaje Nuevo
# =================================================================
class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'mensajes/enviar_mensaje.html'
    success_url = reverse_lazy('bandeja_entrada')

    # ➡️ AÑADIDO: Método para precargar campos desde la URL (para la función 'Responder')
    def get_initial(self):
        initial = super().get_initial()
        
        # 1. Precargar Asunto
        if 'asunto' in self.request.GET:
            initial['asunto'] = self.request.GET.get('asunto')
        
        # 2. Precargar Receptor
        nombre_receptor = self.request.GET.get('receptor')
        if nombre_receptor:
            try:
                # Buscamos el objeto User y lo precargamos
                receptor_user = User.objects.get(username=nombre_receptor)
                initial['receptor'] = receptor_user 
            except User.DoesNotExist:
                pass
                
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)


# =================================================================
# 🔑 CBV 3: Detalle de Mensaje
# =================================================================
class MensajeDetailView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'mensajes/detalle_mensaje.html'
    context_object_name = 'mensaje'
    
    def get(self, request, *args, **kwargs):
        mensaje = self.get_object()
        
        # Marcamos como leído si el usuario actual es el receptor y no ha sido leído
        if mensaje.receptor == request.user and not mensaje.leido:
            mensaje.leido = True
            # ➡️ MODIFICACIÓN: Añadir la fecha de lectura
            mensaje.fecha_lectura = timezone.now()
            mensaje.save()
            
            
        return super().get(request, *args, **kwargs)