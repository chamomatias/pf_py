from django import forms
from docentes.models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'email', 'materia']
        labels = {
            'nombre': 'Nombre del Docente',
            'apellido': 'Apellido del Docente',
            'email': 'Correo Electrónico',
            'materia': 'Materia que imparte',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del docente',
            'apellido': 'Ingrese el apellido del docente',
            'email': 'Ingrese el correo electrónico del docente',
            'materia': 'Ingrese la materia que imparte el docente',
        }