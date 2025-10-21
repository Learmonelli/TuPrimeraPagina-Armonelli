from django.shortcuts import render
from django.http import HttpResponse

from .models import Autor, Categoria, Post
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaPostFormulario

# --------------------------
# Vistas Generales
# --------------------------

def inicio(request):
    """Página de inicio que lista los últimos posts."""
    posts = Post.objects.all().order_by('-fecha_creacion')[:5] # Muestra los 5 más recientes
    contexto = {'posts': posts}
    return render(request, "blog/inicio.html", contexto)

# --------------------------
# Vistas de Creación (CRUD - Create)
# --------------------------

def crear_autor(request):
    if request.method == 'POST':
        formulario = AutorFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Autor.objects.create(
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                email=datos['email']
            )
            return render(request, "blog/inicio.html", {"mensaje": "Autor creado con éxito"})
    else:
        formulario = AutorFormulario()
    
    return render(request, "blog/crear_autor.html", {"formulario": formulario})

def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Categoria.objects.create(
                nombre=datos['nombre'],
                descripcion=datos['descripcion']
            )
            return render(request, "blog/inicio.html", {"mensaje": "Categoría creada con éxito"})
    else:
        formulario = CategoriaFormulario()
    
    return render(request, "blog/crear_categoria.html", {"formulario": formulario})

def crear_post(request):
    if request.method == 'POST':
        formulario = PostFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            try:
                autor = Autor.objects.get(id=datos['autor_id'])
                categoria = Categoria.objects.get(id=datos['categoria_id'])
                
                Post.objects.create(
                    titulo=datos['titulo'],
                    subtitulo=datos['subtitulo'],
                    cuerpo=datos['cuerpo'],
                    fecha_creacion=datos['fecha_creacion'],
                    autor=autor,
                    categoria=categoria
                )
                return render(request, "blog/inicio.html", {"mensaje": "Post creado con éxito"})
            
            except Autor.DoesNotExist:
                mensaje = "Error: El ID del Autor no existe."
            except Categoria.DoesNotExist:
                mensaje = "Error: El ID de la Categoría no existe."
            
            return render(request, "blog/crear_post.html", {"formulario": formulario, "mensaje": mensaje})
    else:
        # Obtener IDs y nombres de Autores y Categorías para ayudar al usuario
        autores = Autor.objects.all()
        categorias = Categoria.objects.all()
        formulario = PostFormulario()
        
    contexto = {
        "formulario": formulario, 
        "autores": autores,
        "categorias": categorias,
        "ayuda_mensaje": "Necesitas el ID de un Autor y una Categoría existentes."
    }
    return render(request, "blog/crear_post.html", contexto)

# --------------------------
# Vistas de Búsqueda
# --------------------------

def buscar_post(request):
    formulario = BusquedaPostFormulario()
    posts_encontrados = []
    criterio = ""

    if request.GET.get("criterio_busqueda"):
        criterio = request.GET["criterio_busqueda"]
        # Filtra Posts cuyo título contenga (icontains) el criterio de búsqueda
        posts_encontrados = Post.objects.filter(titulo__icontains=criterio)
        
    contexto = {
        'formulario': formulario,
        'posts': posts_encontrados,
        'criterio': criterio
    }

    return render(request, 'blog/buscar_post.html', contexto)

