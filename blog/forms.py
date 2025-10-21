from django import forms

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