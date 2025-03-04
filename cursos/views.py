from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from cursos.models import Curso
from cursos.forms import CursoForm

from django.contrib.auth.mixins import LoginRequiredMixin



class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cursos/cursos-listar.html'  # Plantilla para listar cursos

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos-form.html'   # Plantilla para crear un curso
    success_url = reverse_lazy('cursos-listar')    # Redirige a la lista tras crear

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/cursos-form.html'   # Puedes reutilizar la misma plantilla de creación
    success_url = reverse_lazy('cursos-listar')

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/cursos-confirmar-borrar.html'  # Plantilla para confirmar la eliminación
    success_url = reverse_lazy('cursos-listar')

class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = 'cursos/cursos-detallar.html'  # Plantilla para ver el detalle del curso
