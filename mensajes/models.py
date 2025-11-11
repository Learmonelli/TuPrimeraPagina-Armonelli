# mensajes/models.py
from django.db import models
from django.contrib.auth.models import User # Importamos el modelo de usuario

class Mensaje(models.Model):
    # Relaciones
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    
    # Contenido
    asunto = models.CharField(max_length=150) # <-- ¡CAMPO AÑADIDO!
    cuerpo = models.TextField(max_length=1000)
    
    # Metadata
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha_envio']
        verbose_name_plural = "Mensajes"

    def __str__(self):
        # Ahora incluimos el asunto para una mejor representación
        return f"De: {self.emisor.username} | Asunto: {self.asunto}"