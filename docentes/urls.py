from django.urls import path
from docentes.views import (
    DocenteListView,
    DocenteCreateView,
    DocenteUpdateView,
    DocenteDeleteView,
    DocenteDetailView,
)

urlpatterns = [
    path('', DocenteListView.as_view(), name='docentes-listar'),
    path('crear/', DocenteCreateView.as_view(), name='docentes-crear'),
    path('<int:pk>/', DocenteDetailView.as_view(), name='docentes-detallar'),
    path('actualizar/<int:pk>/', DocenteUpdateView.as_view(), name='docentes-actualizar'),
    path('borrar/<int:pk>/', DocenteDeleteView.as_view(), name='docentes-borrar'),
]
