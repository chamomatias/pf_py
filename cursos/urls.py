from django.urls import path
from cursos.views import (
    CursoListView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView,
    CursoDetailView
)

urlpatterns = [
    path('', CursoListView.as_view(), name='cursos-listar'),
    path('crear/', CursoCreateView.as_view(), name='cursos-crear'),
    path('<int:pk>/', CursoDetailView.as_view(), name='cursos-detallar'),
    path('actualizar/<int:pk>/', CursoUpdateView.as_view(), name='cursos-actualizar'),
    path('borrar/<int:pk>/', CursoDeleteView.as_view(), name='cursos-borrar'),
]
