from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Autor, Categoria, Post 
from .forms import (
    AutorFormulario,
    CategoriaFormulario,
    PostFormulario, 
    BusquedaPostFormulario, 
)

# =================================================================
# 1. VISTAS GENERALES Y DE CONTENIDO (PÚBLICAS)
# =================================================================

class PostListView(ListView):
    model = Post
    template_name = 'inicio.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-fecha_creacion')[:5]

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    contexto = {'post': post}
    return render(request, 'detalle_post.html', contexto)

def about(request):
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
# 2. VISTAS DE CREACIÓN/MANIPULACIÓN (CRUD - FBV & CBV)
# =================================================================

@login_required 
def crear_autor(request):
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
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría creada con éxito.')
            return redirect('inicio')
    else:
        formulario = CategoriaFormulario()
    return render(request, "crear_categoria.html", {"formulario": formulario})

# 🔑 CBV con Mixin: (LoginRequiredMixin)
class PostCrearCBV(LoginRequiredMixin, CreateView): 
    model = Post
    form_class = PostFormulario
    template_name = 'crear_post.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # Asigna el usuario logueado como creador del post (por username)
        form.instance.creado_por = self.request.user.username
        messages.success(self.request, f'Post "{form.instance.titulo}" creado con éxito.')
        return super().form_valid(form)

# Vista de Edición (Faltaba su definición en tu código inicial)
@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # ⚠️ Seguridad: Solo el creador puede editar
    if request.user.username != post.creado_por:
        messages.error(request, "No tienes permiso para editar este post.")
        return redirect('detalle_post', pk=post.pk)

    if request.method == 'POST':
        formulario = PostFormulario(request.POST, instance=post)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Post "{post.titulo}" actualizado con éxito.')
            return redirect('detalle_post', pk=post.pk)
    else:
        formulario = PostFormulario(instance=post)
        
    return render(request, 'crear_post.html', {'formulario': formulario}) # Reutiliza la plantilla de creación

# Vista de Eliminación (Faltaba su definición en tu código inicial)
@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # ⚠️ Seguridad: Solo el creador puede eliminar
    if request.user.username != post.creado_por:
        messages.error(request, "No tienes permiso para eliminar este post.")
        return redirect('detalle_post', pk=post.pk)
        
    if request.method == 'POST':
        post.delete()
        messages.warning(request, f'Post "{post.titulo}" eliminado permanentemente.')
        return redirect('inicio')
    
    return render(request, 'eliminar_post.html', {'post': post})