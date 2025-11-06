from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
# Formulario para crear un Autor
class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

# Formulario para crear una Categoria
class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=256)

# Formulario para crear un Post
class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=256)
    cuerpo = forms.CharField(widget=forms.Textarea)
    fecha_creacion = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    # Para Autor y Categoria, usaremos Selects en la vista. Por simplicidad, aquí solo listamos los campos.
    autor_id = forms.IntegerField() 
    categoria_id = forms.IntegerField()

# Formulario para la Búsqueda
class BusquedaPostFormulario(forms.Form):
    criterio_busqueda = forms.CharField(max_length=100, label='Buscar Post por Título')

    

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }