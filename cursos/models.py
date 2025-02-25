from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    duracion_semanas = models.PositiveIntegerField(null=True, blank=True, help_text="Duración en semanas")

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.fecha_inicio} - {self.duracion_semanas} semanas"
