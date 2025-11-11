from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy 

# Importaciones para CBV y Mixin
from django.views.generic import ListView, CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Importaciones de Modelos y Formularios
from .models import Autor, Categoria, Post, Avatar 
from .forms import (
    AutorFormulario, 
    CategoriaFormulario, 
    PostFormulario, 
    BusquedaPostFormulario, 
    AvatarForm, 
    EdicionPerfilForm 
)


# =================================================================
# 1. VISTAS GENERALES Y DE CONTENIDO (PÚBLICAS)
# =================================================================

# 🔑 VISTA BASADA EN CLASES (CBV 1: Listado de Posts)
class PostListView(ListView):
    # ... (código ListView sin cambios)
    model = Post
    template_name = 'inicio.html'
    context_object_name = 'posts'
    # Limita a 5 posts, ordenados por fecha descendente
    queryset = Post.objects.all().order_by('-fecha_creacion')[:5] 


def detalle_post(request, pk):
    """Muestra el detalle de un post específico."""
    post = get_object_or_404(Post, pk=pk)
    contexto = {'post': post}
    return render(request, 'detalle_post.html', contexto)


def about(request):
    """Vista de la página 'Acerca de mí'."""
    return render(request, 'about.html')


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
# 2. VISTAS DE AUTENTICACIÓN Y PERFIL (FBV)
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

@login_required 
def perfil(request):
    """Muestra la información básica del usuario logueado, incluyendo el Avatar."""
    try:
        avatar = request.user.avatar 
    except Avatar.DoesNotExist:
        avatar = None 
        
    return render(request, 'perfil.html', {'avatar': avatar})
    
@login_required 
def editarPerfil(request):
    if request.method == 'POST':
        form = EdicionPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil') 
    else:
        form = EdicionPerfilForm(instance=request.user)
        
    return render(request, 'editarPerfil.html', {'form': form})

@login_required
def agregarAvatar(request): 
    avatar_instancia, created = Avatar.objects.get_or_create(user=request.user) 

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar_instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar actualizado con éxito.')
            return redirect('perfil') 
    else:
        form = AvatarForm(instance=avatar_instancia)
        
    return render(request, 'agregar_avatar.html', {'form': form})


# =================================================================
# 3. VISTAS DE CREACIÓN/MANIPULACIÓN (CRUD - FBV & CBV)
# =================================================================

@login_required 
def crear_autor(request):
    # ... (código crear_autor sin cambios)
    if request.method == 'POST':
        formulario = AutorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, 'Autor creado con éxito.')
            return redirect('inicio') 
    else:
        formulario = AutorFormulario()
    
    return render(request, "crear_autor.html", {"formulario": formulario})

@login_required 
def crear_categoria(request):
    # ... (código crear_categoria sin cambios)
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, 'Categoría creada con éxito.')
            return redirect('inicio')
    else:
        formulario = CategoriaFormulario()
    
    return render(request, "crear_categoria.html", {"formulario": formulario})


# 🔑 CORRECCIÓN APLICADA: Se eliminó el @login_required solitario aquí.

class PostCrearCBV(LoginRequiredMixin, CreateView): 
# ^^^^^^^^^^^^^^^ Nombre nuevo
    model = Post
    form_class = PostFormulario
    template_name = 'crear_post.html'
    
    success_url = reverse_lazy('inicio') 

    def form_valid(self, form):
        # Asigna el usuario actual al campo 'creado_por'
        form.instance.creado_por = self.request.user
        messages.success(self.request, 'Post creado con éxito.')
        
        # Redirigir al detalle del nuevo post
        self.success_url = reverse_lazy('detalle_post', kwargs={'pk': form.instance.pk})
        return super().form_valid(form)


@login_required 
def editar_post(request, pk):
    # ... (código editar_post sin cambios)
    post = get_object_or_404(Post, pk=pk)

    if post.creado_por != request.user:
        messages.error(request, "No tienes permiso para editar este post.")
        return redirect('detalle_post', pk=post.pk)

    if request.method == 'POST':
        formulario = PostFormulario(request.POST, instance=post) 
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Post actualizado con éxito.')
            return redirect('detalle_post', pk=post.pk) 
    else:
        formulario = PostFormulario(instance=post)
        
    contexto = {
        "formulario": formulario,
        "post": post 
    }
    return render(request, "editar_post.html", contexto)


@login_required 
def eliminar_post(request, pk):
    # ... (código eliminar_post sin cambios)
    post = get_object_or_404(Post, pk=pk)

    if post.creado_por != request.user:
        messages.error(request, "No tienes permiso para eliminar este post.")
        return redirect('detalle_post', pk=post.pk)

    if request.method == 'POST':
        post.delete()
        messages.warning(request, f'El post "{post.titulo}" ha sido eliminado permanentemente.')
        return redirect('inicio')
        
    contexto = {"post": post}
    return render(request, "eliminar_post.html", contexto)