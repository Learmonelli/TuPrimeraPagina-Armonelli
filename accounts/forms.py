# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar 

# =========================================================
# 1. Registro de Usuarios
# =========================================================
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) 


# =========================================================
# 2. Edición de Perfil (Para la vista editarPerfil)
# =========================================================
class EdicionPerfilForm(UserChangeForm):
    password = None # Excluye el campo password
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


# =========================================================
# 3. Formulario de Avatar (Para la vista agregarAvatar)
# =========================================================
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']