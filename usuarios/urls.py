from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from usuarios import views
from usuarios.views import SobreMiView

from usuarios.views import UsuarioCreate, UsuarioList, UsuarioUpdate, UsuarioDelete, mi_perfil




urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('inicio')), name="users-logout"),
    path("sobre-mi/", SobreMiView.as_view(), name="sobre-mi"),
    path("crear/", UsuarioCreate.as_view(), name="users-crear"),
    path("listar/", UsuarioList.as_view(), name="users-listar"),
    path("editar/<int:pk>/", UsuarioUpdate.as_view(), name="users-editar"),
    path("eliminar/<int:pk>/", UsuarioDelete.as_view(), name="users-eliminar"),
    path("perfil/", mi_perfil, name="users-perfil"),


]

