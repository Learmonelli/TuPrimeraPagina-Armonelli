
TuPrimeraPagina-Armonelli 📝
Proyecto Web Django: Blog Completo (Patrón MVT)
Este proyecto es una aplicación web tipo blog desarrollada con Python y Django que cumple con todos los requisitos de la entrega final. Incluye un CRUD completo para posts, gestión de perfiles de usuario, implementación de Vistas Basadas en Clases (CBVs) y una aplicación de mensajería privada.



✨ Funcionalidades Implementadas

| Área | Funcionalidad | Descripción |
|------|----------------|--------------|
| **Páginas** | Inicio (`/`), Acerca de Mí (`/about/`) y Detalle de Post (`/pages/<id>/`) | Vistas de navegación principales. |
| **CRUD Posts** | Creación, edición, detalle y eliminación de entradas | Lógica completa y segura: solo el autor puede editar o eliminar sus posts. |
| **Vistas Avanzadas** | Uso de 2 CBVs y 1 Mixin | Implementa `PostListView`, `PostCreateView` y `LoginRequiredMixin`. |
| **Autenticación** | Registro, login, logout y cambio de contraseña | Flujo de usuario completo gestionado a través de la app de Cuentas/Perfiles. |
| **Perfiles** | Vista de perfil, edición de datos y gestión de **Avatar** | Permite personalizar la información del usuario y subir una foto de perfil. |
| **Mensajería** | Envío y recepción de mensajes privados | Incluye bandeja de entrada y envío entre usuarios. |
| **Búsqueda** | Búsqueda de posts por título | Formulario funcional de búsqueda parcial. |
| **Admin** | Administración completa de modelos | Todos los modelos (`Post`, `Autor`, `Categoria`, `Avatar`, `Mensaje`) registrados en el panel de administración. |

---

## 🛠️ Requisitos Técnicos y Estructurales

- **Patrón MVT:** Estructura que sigue las convenciones de Django (Modelos, Vistas, Templates). 
- **Herencia de Templates:** Uso de `base.html` con bloques (`block`) para una estructura visual consistente. 
- **Seguridad:** Las vistas CRUD y de perfil están protegidas con `@login_required` o `LoginRequiredMixin`. 
- **Archivos ignorados (.gitignore):** Se excluyen correctamente `__pycache__`, `db.sqlite3` y la carpeta `media/`. 
- **Dependencias:** El archivo `requirements.txt` contiene todas las bibliotecas necesarias para ejecutar el proyecto.

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone [https://github.com/usuario/TuPrimeraPagina-Armonelli.git](https://github.com/usuario/TuPrimeraPagina-Armonelli.git)
cd TuPrimeraPagina-Armonelli


🧩 Orden de Prueba de FuncionalidadesPara evitar errores de clave foránea y garantizar un flujo de prueba coherente, seguí este orden:#FuncionalidadURL RelativaNotas1Registro de usuarios/registro/Crear al menos dos usuarios para probar la mensajería.2Crear Autor y Categoría/autor/crear/ y /categoria/crear/Requeridos antes de crear un post.3Crear Post/post/crear/Usa la vista PostCreateView (CBV con Mixin).4Editar o Borrar Post/pages/<id>/Solo el autor puede ver los enlaces de edición/eliminación.5Mensajería/mensajeria/enviar/ y /mensajeria/bandeja/Probar el envío de mensajes entre los dos usuarios.6Perfil y Avatar/perfil/Probar la edición de datos y subida de imagen.7Búsqueda de Posts/post/buscar/Probar búsqueda parcial por título.8Inicio/Confirmar que se muestren los últimos posts usando PostListView.

Estructura

TuPrimeraPagina-Armonelli/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── TuPrimeraPagina/     # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── blog/                # App principal (Posts, Categorías, Autores)
├── accounts/            # App para Autenticación (Registro, Login, Logout)
├── perfiles/            # App para gestión de Perfiles y Avatares
├── mensajes/            # App de mensajes privados entre usuarios
└── templates/           # Carpeta de templates base y extendidos

💡 Autor
Leandro Armonelli 📚 Sociólogo y analista de datos, entusiasta de la tecnología, la lectura y la música. Proyecto desarrollado para la Entrega Final del Curso de Python con Django.

