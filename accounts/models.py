from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Cada usuario tiene un único avatar
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Carpeta donde se guardan las imágenes

    def __str__(self):
        return f"Avatar de {self.user.username}"  # Muestra algo legible en el admin
