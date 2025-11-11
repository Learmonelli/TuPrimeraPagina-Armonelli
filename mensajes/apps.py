# mensajes/apps.py

from django.apps import AppConfig

# Renombra la clase si aún se llama MensajeriaConfig
class MensajesConfig(AppConfig):
    # ¡Asegúrate de que el name sea 'mensajes'!
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mensajes' 
    # El verbose_name es opcional, pero debe reflejar el nombre si lo usas
    verbose_name = 'Mensajes'