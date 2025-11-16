from django.contrib import admin
from .models import Autor, Categoria, Post

# Asegúrate de que SÓLO importes los modelos de Blog: Autor, Categoria, Post.
# La importación de Avatar DEBE ser eliminada.

# Opcional: Registra los modelos con la configuración predeterminada
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)

# Si tienes clases Admin personalizadas, asegúrate de que no contengan Avatar.

