from django.contrib import admin
from .models import Autor, Categoria, Post, Avatar

# 1. Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')

# 2. Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

# 3. Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion', 'creado_por')
    search_fields = ('titulo', 'cuerpo', 'autor__nombre') 
    list_filter = ('categoria', 'fecha_creacion')
    # Opcional: Rellenar 'creado_por' automáticamente al guardar
    def save_model(self, request, obj, form, change):
        if not obj.creado_por:
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

# 4. Avatar
@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')