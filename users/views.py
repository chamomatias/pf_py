from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from users.forms import RegistroUsuarioForm, EditarUsuarioForm






from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import PerfilUsuario

class LoginUsuarioView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        user = form.get_user()

        # Verificar si el usuario tiene un perfil, si no, crearlo
        if not hasattr(user, 'perfilusuario'):
            PerfilUsuario.objects.create(user=user)
            messages.info(self.request, "Se creó un perfil de usuario automáticamente.")

        # Iniciar sesión
        login(self.request, user)
        messages.success(self.request, "Has iniciado sesión correctamente.")
        return redirect('inicio')

    def form_invalid(self, form):
        messages.error(self.request, "Error en el inicio de sesión. Verifica tus credenciales.")
        return self.render_to_response(self.get_context_data(form=form))



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
