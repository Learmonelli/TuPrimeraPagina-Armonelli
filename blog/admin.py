from django.contrib import admin
from .models import Autor, Categoria, Post

# ----------------------------------
# CLASES ADMIN PERSONALIZADAS
# ----------------------------------

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('apellido',)
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion', 'creado_por')
    search_fields = ('titulo', 'contenido', 'creado_por')
    list_filter = ('categoria', 'fecha_creacion', 'autor')
    # Permite ordenar los campos en la vista de detalle del post
    fieldsets = (
        (None, {'fields': ('titulo', 'subtitulo', 'contenido', 'imagen')}),
        ('Relaciones', {'fields': ('autor', 'categoria')}),
    )
    # Hace que 'creado_por' sea de solo lectura, ya que lo llenamos en la vista
    readonly_fields = ('creado_por', 'fecha_creacion') 


# ----------------------------------
# REGISTRO DE MODELOS
# ----------------------------------

# Usamos las clases personalizadas para registrar:
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)