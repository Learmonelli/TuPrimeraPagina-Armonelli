from django.db import models

# --- Modelos de Contenido ---

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    # Si querés, podés agregar descripción opcional:
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    
    # 🚨 ADICIÓN CLAVE: Campo 'subtitulo' requerido por las plantillas
    subtitulo = models.CharField(max_length=200, default='Un artículo interesante para el blog.')
    
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # El campo 'creado_por' almacena el 'username' del usuario que publica.
    creado_por = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return self.titulo