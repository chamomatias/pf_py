from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.views.generic import TemplateView


from django.http import HttpResponseRedirect


from django.contrib import messages









class SobreMiView(TemplateView):
    template_name = "usuarios/sobre-mi.html"


from django.contrib import messages

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "/")
                messages.success(request, "¡Bienvenido, {}!".format(usuario))
                return HttpResponseRedirect(next_url)
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")

    form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})




from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.forms import UsuarioForm

# Crear usuario
class UsuarioCreate(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/usuarios-crear.html"
    success_url = reverse_lazy("users-listar")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])  # Hashear la contraseña
        user.save()
        return super().form_valid(form)

# Listar usuarios
class UsuarioList(ListView):
    model = User
    template_name = "usuarios/usuarios-listar.html"
    context_object_name = "usuarios"

# Actualizar usuario
class UsuarioUpdate(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuarios/usuarios-editar.html"
    success_url = reverse_lazy("users-listar")

# Eliminar usuario
class UsuarioDelete(DeleteView):
    model = User
    template_name = "usuarios/usuarios-eliminar.html"
    success_url = reverse_lazy("users-listar")
    

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.forms import UsuarioUpdateForm, PerfilUsuarioForm, CambiarPasswordForm
from usuarios.models import PerfilUsuario
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def mi_perfil(request):
    usuario = request.user
    perfil, created = PerfilUsuario.objects.get_or_create(user=usuario)

    if request.method == "POST":
        user_form = UsuarioUpdateForm(request.POST, instance=usuario)
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        password_form = CambiarPasswordForm(request.POST)

        if "update_info" in request.POST:
            if user_form.is_valid() and perfil_form.is_valid():
                user_form.save()
                perfil_form.save()
                messages.success(request, "Perfil actualizado correctamente.")
                return redirect("users-perfil")

        elif "update_password" in request.POST:
            if password_form.is_valid():
                actual = password_form.cleaned_data["password_actual"]
                nueva = password_form.cleaned_data["nueva_password"]
                confirmar = password_form.cleaned_data["confirmar_password"]

                if usuario.check_password(actual):
                    if nueva == confirmar:
                        usuario.set_password(nueva)
                        usuario.save()
                        update_session_auth_hash(request, usuario)  # Evita cerrar la sesión
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

