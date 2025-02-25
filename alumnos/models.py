from django.db import models

class Alumnos(models.Model):
    # Django crea automáticamente un campo 'id' (clave primaria)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        # Se muestra el ID junto con el nombre, apellido y email del alumno
        return f"{self.id} - {self.nombre} {self.apellido} - {self.email}"
