from django.urls import path
from cursos.views import (
    CursoListView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView,
    CursoDetailView
)

urlpatterns = [
    # Vista para listar todos los cursos
    path('', CursoListView.as_view(), name='cursos-listar'),
    
    # Vista para crear un nuevo curso
    path('crear/', CursoCreateView.as_view(), name='cursos-crear'),
    
    # Vista para mostrar el detalle de un curso
    path('<int:pk>/', CursoDetailView.as_view(), name='cursos-detallar'),
    
    # Vista para actualizar la información de un curso
    path('actualizar/<int:pk>/', CursoUpdateView.as_view(), name='cursos-actualizar'),
    
    # Vista para eliminar un curso
    path('borrar/<int:pk>/', CursoDeleteView.as_view(), name='cursos-borrar'),
]
