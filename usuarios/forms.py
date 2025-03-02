from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "password"]


from django import forms
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ["avatar"]

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class CambiarPasswordForm(forms.Form):
    password_actual = forms.CharField(widget=forms.PasswordInput, label="Contraseña Actual")
    nueva_password = forms.CharField(widget=forms.PasswordInput, label="Nueva Contraseña")
    confirmar_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
