from django.shortcuts import render, redirect 
from django.http import HttpResponse 

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.decorators import login_required 

# Importaciones de Modelos y Formularios de tu aplicación
from .models import Autor, Categoria, Post, Avatar 
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaPostFormulario, AvatarForm
from django.shortcuts import render, redirect, get_object_or_404


# =================================================================
# 1. VISTAS GENERALES Y DE CONTENIDO
# =================================================================

def inicio(request):
    """Página de inicio que lista los últimos posts."""
    posts = Post.objects.all().order_by('-fecha_creacion')[:5] 
    contexto = {'posts': posts}
    return render(request, "inicio.html", contexto)


# =================================================================
# 2. VISTAS DE CREACIÓN (CRUD - Create)
# =================================================================
# ... (crear_autor, crear_categoria, crear_post - sin cambios)

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

def about(request):
    """Vista de la página 'Acerca de mí'."""
    return render(request, 'about.html')

@login_required 
def editarPerfil(request):
    form_class = UserChangeForm 
    
    if request.method == 'POST':
        form = form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil') 
    else:
        form = form_class(instance=request.user)
        
    return render(request, 'editarPerfil.html', {'form': form})


@login_required 
def perfil(request):
    """Muestra la información básica del usuario logueado."""
    # Simplemente renderizamos una plantilla con la información del usuario
    return render(request, 'perfil.html', {})
    
    
@login_required
def agregarAvatar(request): # 🌟 VISTA PARA GESTIONAR EL AVATAR
    try:
        # Intenta obtener la instancia de Avatar existente para el usuario
        avatar_instancia = request.user.avatar
    except:
        # Si no existe (es la primera vez que sube), crea un objeto sin guardar
        avatar_instancia = Avatar(user=request.user) 

    if request.method == 'POST':
        # Pasamos la data, los archivos (request.FILES) y la instancia
        form = AvatarForm(request.POST, request.FILES, instance=avatar_instancia)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            messages.success(request, 'Avatar actualizado con éxito.')
            return redirect('perfil') 
    else:
        form = AvatarForm(instance=avatar_instancia)
        
    return render(request, 'agregar_avatar.html', {'form': form})