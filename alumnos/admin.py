from django.contrib import admin
from .models import Alumnos

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')

admin.site.register(Alumnos, AlumnosAdmin)
