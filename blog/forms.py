from django import forms
from .models import Autor, Categoria, Post

# =================================================================
# 1. Formularios de CRUD (Usando ModelForm para la Base de Datos)
# =================================================================

class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'email')

class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        # Excluimos campos automáticos que se llenan en views.py
        exclude = ('creado_por', 'fecha_creacion')
        widgets = {
            'contenido': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

# =================================================================
# 2. Formulario de Búsqueda de Posts
# =================================================================

class BusquedaPostFormulario(forms.Form):
    criterio_busqueda = forms.CharField(max_length=100, label='Buscar Post por Título')