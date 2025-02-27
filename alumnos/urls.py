from django.urls import path
from alumnos.views import (
    AlumnosListView,
    AlumnosCreateView,
    AlumnosUpdateView,
    AlumnosDeleteView,
    AlumnosDetailView,
)

urlpatterns = [
    # Vista para listar todos los alumnos
    path('', AlumnosListView.as_view(), name='alumnos-listar'),
    
    # Vista para crear un nuevo alumno
    path('crear/', AlumnosCreateView.as_view(), name='alumnos-crear'),
    
    # Vista para mostrar el detalle de un alumno
    path('<int:pk>/', AlumnosDetailView.as_view(), name='alumnos-detallar'),
    
    # Vista para actualizar la información de un alumno
    path('actualizar/<int:pk>/', AlumnosUpdateView.as_view(), name='alumnos-actualizar'),
    
    # Vista para eliminar un alumno
    path('borrar/<int:pk>/', AlumnosDeleteView.as_view(), name='alumnos-borrar'),
]
