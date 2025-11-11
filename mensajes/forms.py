# mensajes/forms.py (CORREGIDO)

from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

# Formulario para crear un nuevo mensaje
class MensajeForm(forms.ModelForm):
    
    class Meta:
        model = Mensaje
        # Excluir 'emisor' y 'leido' ya que se gestionan automáticamente en la vista
        # AÑADIR 'asunto'
        fields = ['receptor', 'asunto', 'cuerpo']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'}),
        }

    # Lógica para Excluir al Usuario Actual de la Lista de Receptores
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        
        super().__init__(*args, **kwargs)
        
        # Filtramos el campo 'receptor'
        if user:
            # Filtra el queryset de receptores para EXCLUIR al usuario actual (user)
            self.fields['receptor'].queryset = User.objects.exclude(pk=user.pk)