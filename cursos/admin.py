from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    # Muestra todos los campos deseados en la lista del admin
    list_display = ('id', 'nombre', 'descripcion', 'fecha_inicio', 'duracion_semanas')
    # Permite hacer clic en los campos id o nombre para editar el registro
    list_display_links = ('id', 'nombre')
    # Agrega filtros y buscador para facilitar la administración
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_inicio',)

admin.site.register(Curso, CursoAdmin)
