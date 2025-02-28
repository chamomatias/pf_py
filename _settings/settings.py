from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Construcción de rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Configuración de seguridad ---
SECRET_KEY = 'django-insecure-(vqi0riobrv3+q0z@4c=b8pi23e7-#rw7g_%%@h%tc70a*6b4@'  # ¡No usar en producción!
DEBUG = True  # Desactivar en producción
ALLOWED_HOSTS = []  # Definir hosts permitidos en producción

# --- Aplicaciones instaladas ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cursos',
    'alumnos',
    'docentes',
    'users',
]

# --- Middleware (gestión de peticiones HTTP) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Configuración de URLs ---
ROOT_URLCONF = '_settings.urls'

# --- Configuración de plantillas ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- Configuración de WSGI ---
WSGI_APPLICATION = '_settings.wsgi.application'

# --- Configuración de base de datos ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Validación de contraseñas ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internacionalización y zona horaria ---
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Archivos estáticos y medios ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- Configuración de sesión ---
SESSION_COOKIE_AGE = 1  # Expira en 1 segundo
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Cierra sesión al cerrar el navegador

# --- Redirección de autenticación ---
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/users/login/'

# --- Configuración de mensajes ---
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
