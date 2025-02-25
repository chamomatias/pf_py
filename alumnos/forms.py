from django import forms
from .models import Alumnos

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'email']
        labels = {
            'nombre': 'Nombre del Alumno',
            'apellido': 'Apellido del Alumno',
            'email': 'Correo Electrónico',
        }
