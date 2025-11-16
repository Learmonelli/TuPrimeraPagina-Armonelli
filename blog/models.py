from django.db import models
from django.contrib.auth.models import User # Necesitas importar User para la FK opcional

# --- Modelos de Contenido ---

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    # Recomendación: Añadir unique=True para el email
    email = models.EmailField(unique=True) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    # Recomendación: Meta para el plural en el Admin
    class Meta:
        verbose_name_plural = "Autores"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True) # Recomendación: Las categorías suelen ser únicas
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, default='Un artículo interesante para el blog.')
    contenido = models.TextField()
    
    # 🖼️ ADICIÓN RECOMENDADA: Campo para Imagen de cabecera del Post
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)

    # 🔗 Relación con Autor (asumo que Autor es para el "dueño" del contenido)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # SET_NULL si eliminas una categoría
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # 🔑 Mejor Opción para el usuario:
    # Si quieres una relación más fuerte que solo el username, usa una ForeignKey al User de Django.
    # Si no, tu actual CharField está bien, pero debes actualizar el formulario para 'exclude' la imagen.
    creado_por = models.CharField(max_length=50, blank=True, null=True) 
    # Opcional, si usaras User: creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_creacion'] # Ordena por fecha de creación descendente