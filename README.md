<<<<<<< HEAD
# TuPrimeraPaginaArmonelli 

## Proyecto Web Django (Patrón MVT)

Este proyecto es una implementación de un blog sencillo desarrollado con Django y el patrón MVT.

Cumple con los siguientes requisitos obligatorios:
1.  Uso de **Herencia de Plantillas** HTML (`base.html`).
2.  Tres **Modelos/Clases** en `models.py`: `Autor`, `Categoria`, y `Post`.
3.  **Formulario de Inserción** de datos para cada modelo.
4.  **Formulario de Búsqueda** sobre la clase `Post`.

## Instalación y Ejecución

## 📋 Orden de Prueba de Funcionalidades

Las funcionalidades deben probarse en el siguiente orden para evitar errores de clave foránea:

| Funcionalidad | URL (Relativa) | Descripción |
| :--- | :--- | :--- |
| **1. Crear Autor** | `/autor/crear/` | Se requiere un autor para poder crear un post. |
| **2. Crear Categoría** | `/categoria/crear/` | Se requiere una categoría para poder crear un post. |
| **3. Crear Post** | `/post/crear/` | Formulario principal. Utiliza los IDs del autor y la categoría creados. |
| **4. Buscar Post** | `/post/buscar/` | Permite buscar posts por el título (búsqueda parcial). |
| **5. Inicio** | `/` | Página principal que muestra el listado de los últimos posts. |
=======
# TuPrimeraPagina-Armonelli
>>>>>>> 7bed4b622a83b04c03b059811894e8facb9b3575
