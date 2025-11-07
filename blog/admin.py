from django.contrib import admin
from .models import Autor, Categoria, Post, Avatar 



admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)

# 2. Modelo de Gestión de Usuarios (Avatar)
admin.site.register(Avatar)