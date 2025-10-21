from django.db import models

# Modelo 1: Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 2: Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre

# Modelo 3: Post
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    fecha_creacion = models.DateField()
    
    # Claves foráneas (relaciones)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} por {self.autor.nombre}"