from django.shortcuts import render, redirect # Importaciones generales de Django
from django.http import HttpResponse # Si la necesitas, aunque 'render' es mejor

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm # Para la vista 'registro'
from django.contrib.auth.decorators import login_required # Para vistas protegidas
from django.contrib.auth.forms import UserChangeForm # O tu formulario personalizado 'EditProfileForm'

# Importaciones de Modelos y Formularios de tu aplicación
from .models import Autor, Categoria, Post
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaPostFormulario
# Asegúrate de importar tu formulario personalizado si lo usas:
# from .forms import EditProfileForm 


# =================================================================
# 1. VISTAS GENERALES Y DE CONTENIDO
# =================================================================

def inicio(request):
    """Página de inicio que lista los últimos posts."""
    posts = Post.objects.all().order_by('-fecha_creacion')[:5] # Muestra los 5 más recientes
    contexto = {'posts': posts}
    return render(request, "inicio.html", contexto)


# =================================================================
# 2. VISTAS DE CREACIÓN (CRUD - Create)
# =================================================================

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
            return render(request, "inicio.html", {"mensaje": "Autor creado con éxito"})
    else:
        formulario = AutorFormulario()
    
    return render(request, "crear_autor.html", {"formulario": formulario})

def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            Categoria.objects.create(
                nombre=datos['nombre'],
                descripcion=datos['descripcion']
            )
            return render(request, "inicio.html", {"mensaje": "Categoría creada con éxito"})
    else:
        formulario = CategoriaFormulario()
    
    return render(request, "crear_categoria.html", {"formulario": formulario})

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
                return render(request, "inicio.html", {"mensaje": "Post creado con éxito"})
            
            except Autor.DoesNotExist:
                mensaje = "Error: El ID del Autor no existe."
            except Categoria.DoesNotExist:
                mensaje = "Error: El ID de la Categoría no existe."
            
            return render(request, "crear_post.html", {"formulario": formulario, "mensaje": mensaje})
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
    return render(request, "crear_post.html", contexto)


# =================================================================
# 3. VISTAS DE BÚSQUEDA
# =================================================================

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

    return render(request, 'buscar_post.html', contexto)


# =================================================================
# 4. VISTAS DE AUTENTICACIÓN Y PERFIL
# =================================================================

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ya puedes iniciar sesión.')
            return redirect('login') 
    else:
        form = UserCreationForm()
        
    return render(request, 'registro.html', {'form': form})


@login_required # con este decorador exigimos que el usuario esté logueado para utilizar esta view
def editarPerfil(request):
    # Si usas tu formulario personalizado 'EditProfileForm', reemplaza UserChangeForm
    # form_class = EditProfileForm 
    form_class = UserChangeForm 
    
    if request.method == 'POST':
        # Se enlaza la data enviada (request.POST) con la instancia del usuario actual
        form = form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save() # Guarda los cambios del usuario
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil') # Redirige a la URL con nombre 'perfil'
    else:
        # Se inicializa el formulario con los datos actuales del usuario
        form = form_class(instance=request.user)
        
    # Renderiza la plantilla, pasando el formulario
    return render(request, 'editarPerfil.html', {'form': form})

@login_required 
def perfil(request):
    """Muestra la información básica del usuario logueado."""
    # Simplemente renderizamos una plantilla con la información del usuario
    return render(request, 'perfil.html', {})