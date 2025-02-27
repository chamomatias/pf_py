from django.urls import path
from .views import (
    LoginUsuarioView, LogoutUsuarioView, RegistroUsuarioView,
    EditarUsuarioView, ListarUsuariosView, DetalleUsuarioView, 
    LogoutMensajeView, CambiarPasswordView, CambioPasswordDoneView, MiPerfilView
)

urlpatterns = [
    # Ruta para iniciar sesión
    path('login/', LoginUsuarioView.as_view(), name='users-login'),
    
    # Ruta para cerrar sesión y redireccionar con mensaje
    path('logout/', LogoutUsuarioView.as_view(), name='users-logout'),
    path('logout/mensaje/', LogoutMensajeView.as_view(), name='users-logout-mensaje'),
    
    # Ruta para registrar un nuevo usuario
    path('registro/', RegistroUsuarioView.as_view(), name='users-registro'),
    
    # Ruta para editar la información del usuario (usando pk)
    path('editar/<int:pk>/', EditarUsuarioView.as_view(), name='users-editar'),
    
    # Ruta para listar todos los usuarios
    path('listar/', ListarUsuariosView.as_view(), name='users-listar'),
    
    # Ruta para ver el detalle de un usuario (usando pk)
    path('<int:pk>/', DetalleUsuarioView.as_view(), name='users-detallar'),
    
    # Rutas para cambiar la contraseña
    path('cambiar-password/', CambiarPasswordView.as_view(), name='users-cambiar-password'),
    path('cambiar-password/done/', CambioPasswordDoneView.as_view(), name='users-cambio-password-done'),
    
    # Ruta para que el usuario vea su propio perfil
    path('mi-perfil/', MiPerfilView.as_view(), name='users-mi-perfil'),
]
