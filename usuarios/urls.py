from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
from usuarios.views import SobreMiView


urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
    path("sobre-mi/", SobreMiView.as_view(), name="users-sobre-mi"),

]

