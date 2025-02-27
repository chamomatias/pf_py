from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from alumnos.models import Alumnos
from alumnos.forms import AlumnosForm


# ---------------------------
# Vistas para la gestión de Alumnos
# ---------------------------

class AlumnosListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los alumnos.
    """
    model = Alumnos
    template_name = 'alumnos/alumnos-listar.html'


class AlumnosCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear un nuevo alumno.
    """
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-form.html'
    success_url = reverse_lazy('alumnos-listar')


class AlumnosUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para actualizar la información de un alumno.
    Reutiliza la misma plantilla que la creación.
    """
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-form.html'
    success_url = reverse_lazy('alumnos-listar')


class AlumnosDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para confirmar y eliminar un alumno.
    """
    model = Alumnos
    template_name = 'alumnos/alumnos-confirmar-borrar.html'
    success_url = reverse_lazy('alumnos-listar')


class AlumnosDetailView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar el detalle de un alumno.
    """
    model = Alumnos
    template_name = 'alumnos/alumnos-detallar.html'
