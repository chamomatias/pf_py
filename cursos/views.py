from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from cursos.models import Curso
from cursos.forms import CursoForm


# ---------------------------
# Vistas para la Gestión de Cursos
# ---------------------------

class CursoListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los cursos.
    """
    model = Curso
    template_name = 'cursos/cursos-listar.html'


class CursoCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear un nuevo curso.
    """
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos-form.html'
    success_url = reverse_lazy('cursos-listar')


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para actualizar la información de un curso.
    Se reutiliza la misma plantilla que en la creación.
    """
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos-form.html'
    success_url = reverse_lazy('cursos-listar')


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para confirmar y eliminar un curso.
    """
    model = Curso
    template_name = 'cursos/cursos-confirmar-borrar.html'
    success_url = reverse_lazy('cursos-listar')


class CursoDetailView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar el detalle de un curso.
    """
    model = Curso
    template_name = 'cursos/cursos-detallar.html'
