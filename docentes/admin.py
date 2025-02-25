from django.contrib import admin
from docentes.models import Docente

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'materia')
    search_fields = ('nombre', 'apellido', 'email', 'materia')

admin.site.register(Docente, DocenteAdmin)
