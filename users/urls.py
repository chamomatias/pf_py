from django.urls import path
from users.views import (
    LoginUsuarioView, LogoutUsuarioView, RegistroUsuarioView,
    EditarUsuarioView, ListarUsuariosView, DetalleUsuarioView, LogoutMensajeView, SobreMiView
    
)

urlpatterns = [
    path('login/', LoginUsuarioView.as_view(), name='users-login'),
    path('logout/', LogoutUsuarioView.as_view(), name='users-logout'),
    path('logout/mensaje/', LogoutMensajeView.as_view(), name='users-logout-mensaje'),
    path('registro/', RegistroUsuarioView.as_view(), name='users-registro'),
    path('editar/<int:pk>/', EditarUsuarioView.as_view(), name='users-editar'),
    path('listar/', ListarUsuariosView.as_view(), name='users-listar'),
    path('<int:pk>/', DetalleUsuarioView.as_view(), name='users-detallar'),
    path("sobre-mi/", SobreMiView.as_view(), name="users-sobre-mi"),
]
