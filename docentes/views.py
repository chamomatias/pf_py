from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from docentes.models import Docente
from docentes.forms import DocenteForm


# ---------------------------
# Vistas para la Gestión de Docentes
# ---------------------------

class DocenteListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los docentes.
    """
    model = Docente
    template_name = 'docentes/docentes-listar.html'


class DocenteCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear un nuevo docente.
    """
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'
    success_url = reverse_lazy('docentes-listar')


class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para actualizar la información de un docente existente.
    """
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'
    success_url = reverse_lazy('docentes-listar')


class DocenteDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para confirmar y eliminar un docente.
    """
    model = Docente
    template_name = 'docentes/docentes-confirmar-borrar.html'
    success_url = reverse_lazy('docentes-listar')


class DocenteDetailView(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar el detalle de un docente.
    """
    model = Docente
    template_name = 'docentes/docentes-detallar.html'
