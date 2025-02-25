from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='perfil_fotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Perfil"
