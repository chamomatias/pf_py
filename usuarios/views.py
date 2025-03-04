from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from usuarios.models import PerfilUsuario
from usuarios.forms import UsuarioForm, UsuarioUpdateForm, PerfilUsuarioForm, CambiarPasswordForm

# ==========================
# Vista para la página "Sobre Mí"
# ==========================
class SobreMiView(TemplateView):
    template_name = "usuarios/sobre-mi.html"

# ==========================
# Login de Usuarios (Vista Basada en Clase)
# ==========================
class UsuarioLoginView(LoginView):
    template_name = "usuarios/usuarios-login.html"

    def form_invalid(self, form):
        """Muestra un mensaje de error si el login falla."""
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

    def get_success_url(self):
        """Redirige al usuario a su perfil tras el login exitoso."""
        return self.get_redirect_url() or reverse_lazy("inicio")

# ==========================
# Logout de Usuarios
# ==========================
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

class UsuarioLogoutView(LogoutView):
    """Cierra la sesión del usuario y lo redirige a la página de 'Sesión Cerrada'."""
    template_name = "usuarios/users-logout-confirm.html"

def logout_usuario(request):
    """Maneja el logout y redirige a la página de 'Sesión Cerrada'."""
    logout(request)
    return redirect("users-logout-confirm")



from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UsuarioLogoutView(LogoutView):
    """Cierra la sesión del usuario y muestra un mensaje de confirmación."""
    next_page = reverse_lazy("inicio")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Has cerrado sesión exitosamente.")
        return super().dispatch(request, *args, **kwargs)




# ==========================
# CRUD de Usuarios (Vistas Basadas en Clases)
# ==========================

# Crear usuario (solo para administradores)
class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/usuarios-crear.html"
    success_url = reverse_lazy("users-listar")

    def form_valid(self, form):
        """Guarda el usuario con la contraseña encriptada."""
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)

# Listar usuarios (requiere autenticación)
class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = "usuarios/usuarios-listar.html"
    context_object_name = "usuarios"

# Actualizar usuario (requiere autenticación)
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/usuarios-editar.html"
    success_url = reverse_lazy("users-listar")

# Eliminar usuario (requiere autenticación)
class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "usuarios/usuarios-eliminar.html"
    success_url = reverse_lazy("users-listar")

# ==========================
# Vista de Perfil de Usuario
# ==========================
@login_required
def mi_perfil(request):
    """Permite a los usuarios ver y actualizar su perfil, cambiar su avatar y modificar su contraseña."""
    usuario = request.user
    perfil, created = PerfilUsuario.objects.get_or_create(user=usuario)

    if request.method == "POST":
        user_form = UsuarioUpdateForm(request.POST, instance=usuario)
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        password_form = CambiarPasswordForm(request.POST)

        # Actualizar información del usuario y avatar
        if "update_info" in request.POST:
            if user_form.is_valid() and perfil_form.is_valid():
                user_form.save()
                perfil_form.save()
                messages.success(request, "Perfil actualizado correctamente.")
                return redirect("users-perfil")

        # Cambio de contraseña
        elif "update_password" in request.POST:
            if password_form.is_valid():
                actual = password_form.cleaned_data["password_actual"]
                nueva = password_form.cleaned_data["nueva_password"]
                confirmar = password_form.cleaned_data["confirmar_password"]

                if usuario.check_password(actual):
                    if nueva == confirmar:
                        usuario.set_password(nueva)
                        usuario.save()
                        update_session_auth_hash(request, usuario)  # Mantiene la sesión activa
                        messages.success(request, "Contraseña cambiada exitosamente.")
                        return redirect("users-perfil")
                    else:
                        messages.error(request, "Las contraseñas no coinciden.")
                else:
                    messages.error(request, "Contraseña actual incorrecta.")

    else:
        user_form = UsuarioUpdateForm(instance=usuario)
        perfil_form = PerfilUsuarioForm(instance=perfil)
        password_form = CambiarPasswordForm()

    return render(request, "usuarios/usuarios-perfil.html", {
        "user_form": user_form,
        "perfil_form": perfil_form,
        "password_form": password_form,
        "perfil": perfil
    })
