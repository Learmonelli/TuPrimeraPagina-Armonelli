from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from accounts.models import Avatar 
from .forms import AvatarForm, EdicionPerfilForm 
from .forms import AvatarForm, EdicionPerfilForm, RegistroUsuarioForm # ⬅️ Añadir este
# =================================================================
# 1. VISTAS DE AUTENTICACIÓN
# =================================================================



def registro(request):
    if request.method == 'POST':
        # ⚠️ USAR EL FORMULARIO PERSONALIZADO AQUÍ
        form = RegistroUsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,'¡Registro exitoso! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        # ⚠️ USAR EL FORMULARIO PERSONALIZADO AQUÍ
        form = RegistroUsuarioForm() 
        
    return render(request,'accounts/registro.html', {'form': form})
# =================================================================
# 2. VISTAS DE PERFIL
# =================================================================

@login_required 
def perfil(request):
    try:
        avatar = request.user.avatar
    except Avatar.DoesNotExist:
        avatar = None 
        
    return render(request,'accounts/perfil.html', {'avatar': avatar})
    
@login_required 
def editarPerfil(request):
    if request.method == 'POST':
        form = EdicionPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            # El email está deshabilitado en el form, por lo que no se guarda.
            form.save() 
            messages.success(request,'Perfil actualizado con éxito.')
            return redirect('perfil')
    else:
        form = EdicionPerfilForm(instance=request.user)
        
    return render(request,'accounts/editarPerfil.html', {'form': form})

@login_required
def agregarAvatar(request): 
    # Obtiene o crea la instancia de Avatar para el usuario actual
    avatar_instancia, created = Avatar.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar_instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar actualizado con éxito.')
            return redirect('perfil')
    else:
        form = AvatarForm(instance=avatar_instancia)
        
    return render(request,'accounts/agregar_avatar.html', {'form': form})
