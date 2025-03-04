from django.urls import path
from usuarios.views import (
    UsuarioLoginView, UsuarioLogoutView,
    UsuarioCreate, UsuarioList, UsuarioUpdate, UsuarioDelete,
    mi_perfil, SobreMiView, TemplateView
)

urlpatterns = [
    # Autenticación
    path("login/", UsuarioLoginView.as_view(), name="users-login"),
    path("logout/", UsuarioLogoutView.as_view(), name="users-logout"),
    path("logout-confirm/", TemplateView.as_view(template_name="usuarios/logout-confirm.html"), name="users-logout-confirm"),


    # Perfil
    path("perfil/", mi_perfil, name="users-perfil"),

    # CRUD de usuarios
    path("crear/", UsuarioCreate.as_view(), name="users-crear"),
    path("listar/", UsuarioList.as_view(), name="users-listar"),
    path("editar/<int:pk>/", UsuarioUpdate.as_view(), name="users-editar"),
    path("eliminar/<int:pk>/", UsuarioDelete.as_view(), name="users-eliminar"),

    # Página Sobre Mí
    path("sobre-mi/", SobreMiView.as_view(), name="sobre-mi"),
]
