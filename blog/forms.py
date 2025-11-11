from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Autor, Categoria, Post, Avatar # Importa todos los modelos

# =================================================================
# 1. Formularios de CRUD (Usando ModelForm para la Base de Datos)
# =================================================================

# 1.1. Formulario para crear un Autor
class AutorFormulario(forms.ModelForm):
    # ¡ModelForm gestiona automáticamente la creación del objeto Autor!
    class Meta:
        model = Autor
        # Incluye todos los campos del modelo Autor
        fields = ('nombre', 'apellido', 'email')

# 1.2. Formulario para crear una Categoria
class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

# 1.3. Formulario para crear un Post
class PostFormulario(forms.ModelForm):
    # ModelForm automáticamente convierte 'autor' y 'categoria'
    # en campos Select (dropdown) que listan los objetos existentes.
    class Meta:
        model = Post
        # Excluimos 'creado_por' y 'fecha_creacion' ya que los llenamos en views.py
        exclude = ('creado_por', 'fecha_creacion')
        
        # Opcional: Personalizar el widget del campo cuerpo para hacerlo más grande
        widgets = {
            'cuerpo': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

# =================================================================
# 2. Formularios de Perfil y Búsqueda
# =================================================================

# 2.1. Formulario para la Búsqueda (Sigue siendo un forms.Form simple, ¡correcto!)
class BusquedaPostFormulario(forms.Form):
    criterio_busqueda = forms.CharField(max_length=100, label='Buscar Post por Título')

# 2.2. Formulario para Avatar (Ya era ModelForm, ¡correcto!)
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

# 2.3. Formulario para Edición de Perfil (Corregido y renombrado)
class EdicionPerfilForm(UserChangeForm):
    # Hereda de UserChangeForm, pero le quitaremos la gestión de contraseña,
    # que es confusa aquí.
    password = None # Elimina el campo de contraseña
    
    class Meta:
        model = User
        # Definimos qué campos se pueden editar
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
        }