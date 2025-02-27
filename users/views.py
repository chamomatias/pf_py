from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView

from users.forms import RegistroUsuarioForm, EditarUsuarioForm
from .models import PerfilUsuario


# -------------------------
# Autenticación
# -------------------------

class LoginUsuarioView(LoginView):
    """
    Vista para iniciar sesión.
    """
    template_name = 'users/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, "Has iniciado sesión correctamente.")
        return redirect('inicio')

    def form_invalid(self, form):
        messages.error(self.request, "Error en el inicio de sesión. Verifica tus credenciales.")
        return self.render_to_response(self.get_context_data(form=form))


class LogoutUsuarioView(LogoutView):
    """
    Vista para cerrar sesión.
    """
    template_name = "users/logout.html"
    next_page = reverse_lazy("users-logout-mensaje")


class LogoutMensajeView(TemplateView):
    """
    Vista para mostrar el mensaje tras cerrar sesión.
    """
    template_name = "users/logout_mensaje.html"


# -------------------------
# Registro de Usuario
# -------------------------

class RegistroUsuarioView(CreateView):
    """
    Vista para registrar un nuevo usuario.
    """
    form_class = RegistroUsuarioForm
    template_name = 'users/registro.html'
    success_url = reverse_lazy('users-login')


# -------------------------
# Gestión de Usuarios (Requiere autenticación)
# -------------------------

class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar el perfil del usuario.
    """
    model = User
    form_class = EditarUsuarioForm
    template_name = 'users/editar_perfil.html'
    success_url = reverse_lazy('users-listar')


class ListarUsuariosView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los usuarios.
    """
    model = User
    template_name = 'users/listar_usuarios.html'


class DetalleUsuarioView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar el detalle de un usuario.
    """
    model = User
    template_name = 'users/detallar_usuario.html'


# -------------------------
# Cambio de Contraseña (Requiere autenticación)
# -------------------------

class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    """
    Vista para cambiar la contraseña del usuario.
    """
    template_name = 'users/cambiar_password.html'
    success_url = reverse_lazy('users-cambio-password-done')


class CambioPasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """
    Vista para confirmar el cambio de contraseña.
    """
    template_name = 'users/cambio_password_done.html'


# -------------------------
# Mi Perfil (Requiere autenticación)
# -------------------------

class MiPerfilView(LoginRequiredMixin, DetailView):
    """
    Vista para que el usuario pueda ver su propio perfil.
    """
    model = User
    template_name = 'users/detallar_usuario.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)
