from django.db import models
from django.contrib.auth.models import User

# --- Modelos de Contenido ---

# 1. Modelo Autor (Persona con información biográfica, no necesariamente un usuario loggeado)
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"Autor: {self.nombre} {self.apellido}"

# 2. Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre

# 3. Modelo Post (Se enlaza con el Autor biográfico)
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    # 💡 Sugerencia: Usar DateTimeField con auto_now_add=True
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    
    # Relación con el modelo Autor
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # Relación con el modelo Categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    # 💡 Sugerencia: Añadir una relación al User para saber QUIÉN creó el Post
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Post: {self.titulo} por {self.autor.nombre}"

# --- Modelos de Usuario ---

# 4. Modelo Avatar (Perfil del usuario loggeado, no del autor biográfico)
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"