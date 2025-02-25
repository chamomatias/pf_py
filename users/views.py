from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from users.forms import RegistroUsuarioForm, EditarUsuarioForm


class LoginUsuarioView(LoginView):
    template_name = 'users/login.html'


class LogoutUsuarioView(LogoutView):
    template_name = "users/logout.html"  # Página que se mostrará al cerrar sesión
    next_page = reverse_lazy("users-logout-mensaje")  # Redirección tras logout

class LogoutMensajeView(TemplateView):
    template_name = "users/logout_mensaje.html"




class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'users/registro.html'
    success_url = reverse_lazy('users-login')

class EditarUsuarioView(UpdateView):
    model = User
    form_class = EditarUsuarioForm
    template_name = 'users/editar_perfil.html'
    success_url = reverse_lazy('users-listar')

class ListarUsuariosView(ListView):
    model = User
    template_name = 'users/listar_usuarios.html'

class DetalleUsuarioView(DetailView):
    model = User
    template_name = 'users/detallar_usuario.html'
