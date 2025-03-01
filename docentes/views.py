from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from docentes.models import Docente
from docentes.forms import DocenteForm

from django.contrib.auth.mixins import LoginRequiredMixin

class DocenteListView(LoginRequiredMixin, ListView):
    model = Docente
    template_name = 'docentes/docentes-listar.html'  # Plantilla para listar docentes

class DocenteCreateView(LoginRequiredMixin, CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'    # Plantilla para crear un docente
    success_url = reverse_lazy('docentes-listar')      # Redirige a la lista tras crear

class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'    # Se reutiliza la misma plantilla de creación/edición
    success_url = reverse_lazy('docentes-listar')      # Redirige a la lista tras actualizar

class DocenteDeleteView(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'docentes/docentes-confirmar-borrar.html'  # Plantilla para confirmar la eliminación
    success_url = reverse_lazy('docentes-listar')              # Redirige a la lista tras eliminar

class DocenteDetailView(LoginRequiredMixin, DetailView):
    model = Docente
    template_name = 'docentes/docentes-detallar.html'  # Plantilla para ver el detalle del docente
