from django.urls import path
from docentes.views import (
    DocenteListView,
    DocenteCreateView,
    DocenteUpdateView,
    DocenteDeleteView,
    DocenteDetailView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Vista para listar todos los docentes
    path('', DocenteListView.as_view(), name='docentes-listar'),
    
    # Vista para crear un nuevo docente
    path('crear/', DocenteCreateView.as_view(), name='docentes-crear'),
    
    # Vista para mostrar el detalle de un docente
    path('<int:pk>/', DocenteDetailView.as_view(), name='docentes-detallar'),
    
    # Vista para actualizar la información de un docente
    path('actualizar/<int:pk>/', DocenteUpdateView.as_view(), name='docentes-actualizar'),
    
    # Vista para eliminar un docente
    path('borrar/<int:pk>/', DocenteDeleteView.as_view(), name='docentes-borrar'),
    
    # Ruta para iniciar sesión utilizando la vista de Login de Django
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
