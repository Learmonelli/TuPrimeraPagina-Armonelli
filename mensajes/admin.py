from django.contrib import admin
from .models import Mensaje

# 1. Creamos una clase para personalizar la vista en el Admin (Opcional pero recomendado)
class MensajeAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista (list_display)
    list_display = ('asunto', 'emisor', 'receptor', 'fecha_envio', 'leido')
    
    # Campos que se pueden usar para filtrar los resultados
    list_filter = ('leido', 'fecha_envio', 'receptor')
    
    # Campos por los que se puede buscar
    search_fields = ('asunto', 'cuerpo', 'emisor__username', 'receptor__username')
    
    # Campos que se pueden editar directamente en la vista de lista (solo booleanos o CharFields cortos)
    list_editable = ('leido',)

# 2. Registramos el modelo usando la clase de administración personalizada
admin.site.register(Mensaje, MensajeAdmin)

# Nota: Si no quieres personalización, podrías usar simplemente:
# admin.site.register(Mensaje)