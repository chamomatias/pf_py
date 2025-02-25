from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'duracion_semanas']
        labels = {
            'nombre': 'Nombre del curso',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha de inicio',
            'duracion_semanas': 'Duración en semanas'
        }