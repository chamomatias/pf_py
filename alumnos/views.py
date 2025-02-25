from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from alumnos.models import Alumnos
from alumnos.forms import AlumnosForm

class AlumnosListView(ListView):
    model = Alumnos
    template_name = 'alumnos/alumnos-listar.html'  # Plantilla para listar alumnos

class AlumnosCreateView(CreateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-form.html'   # Plantilla para crear un alumno
    success_url = reverse_lazy('alumnos-listar')    # Redirige a la lista tras crear

class AlumnosUpdateView(UpdateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'alumnos/alumnos-form.html'   # Reutiliza la misma plantilla de creación/edición
    success_url = reverse_lazy('alumnos-listar')    # Redirige a la lista tras actualizar

class AlumnosDeleteView(DeleteView):
    model = Alumnos
    template_name = 'alumnos/alumnos-confirmar-borrar.html'  # Plantilla para confirmar la eliminación
    success_url = reverse_lazy('alumnos-listar')             # Redirige a la lista tras eliminar

class AlumnosDetailView(DetailView):
    model = Alumnos
    template_name = 'alumnos/alumnos-detallar.html'  # Plantilla para ver el detalle del alumno
