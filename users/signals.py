from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilUsuario

# 📌 Cuando se crea un nuevo usuario, también se crea su perfil automáticamente
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)

# 📌 Guardar automáticamente el perfil cuando se guarda el usuario
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfilusuario.save()
