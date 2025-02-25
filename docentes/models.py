from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    materia = models.CharField(max_length=100, null=True, blank=True, help_text="Materia que imparte")

    def __str__(self):
        # Mostramos el id junto con el nombre, apellido y la materia
        return f"{self.id} - {self.nombre} {self.apellido} - ({self.materia} - {self.email})"
