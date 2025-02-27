from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from docentes.models import Docente
from docentes.forms import DocenteForm

class DocenteListView(LoginRequiredMixin, ListView):
    model = Docente
    template_name = 'docentes/docentes-listar.html'

class DocenteCreateView(LoginRequiredMixin, CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'
    success_url = reverse_lazy('docentes-listar')

class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'docentes/docentes-form.html'
    success_url = reverse_lazy('docentes-listar')

class DocenteDeleteView(LoginRequiredMixin, DeleteView):
    model = Docente
    template_name = 'docentes/docentes-confirmar-borrar.html'
    success_url = reverse_lazy('docentes-listar')

class DocenteDetailView(LoginRequiredMixin, DetailView):
    model = Docente
    template_name = 'docentes/docentes-detallar.html'
