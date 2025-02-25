from django.urls import path
from alumnos.views import (
    AlumnosListView,
    AlumnosCreateView,
    AlumnosUpdateView,
    AlumnosDeleteView,
    AlumnosDetailView,
)

urlpatterns = [
    path('', AlumnosListView.as_view(), name='alumnos-listar'),
    path('crear/', AlumnosCreateView.as_view(), name='alumnos-crear'),
    path('<int:pk>/', AlumnosDetailView.as_view(), name='alumnos-detallar'),
    path('actualizar/<int:pk>/', AlumnosUpdateView.as_view(), name='alumnos-actualizar'),
    path('borrar/<int:pk>/', AlumnosDeleteView.as_view(), name='alumnos-borrar'),
]
