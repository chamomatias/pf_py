# San Luis - Big Data

San Luis - Big Data es una plataforma web para la gestión de capacitaciones en diversas tecnologías, incluyendo Python, Power BI, Tableau, SQL e Inteligencia Artificial. La aplicación está desarrollada con Django y utiliza Bootstrap para el diseño de la interfaz.

## Tecnologías utilizadas

- **Django**: Framework web en Python.
- **Bootstrap**: Framework de diseño para la interfaz de usuario.
- **FontAwesome**: Íconos para mejorar la presentación.
- **HTML/CSS/JavaScript**: Tecnologías web estándar.

## Instalación

### Requisitos previos
- Python 3.x
- Django
- Pipenv o virtualenv (opcional pero recomendado)

### Pasos
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```
2. Crear y activar un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configurar la base de datos y aplicar migraciones:
   ```sh
   python manage.py migrate
   ```
5. Crear un superusuario:
   ```sh
   python manage.py createsuperuser
   ```
6. Correr el servidor:
   ```sh
   python manage.py runserver
   ```

## Uso
- Acceder a la aplicación en `http://127.0.0.1:8000/`.
- Iniciar sesión como superusuario para administrar capacitaciones, docentes y alumnos.

## Estructura del Proyecto
```
proy_py/
├── settings/              # Configuración de Django
├── users/                 # Gestión de usuarios
├── cursos/                # Módulo de capacitaciones
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── templates/             # Plantillas HTML
├── manage.py              # Script para ejecutar Django
└── README.md              # Este archivo
```

## Contribuciones
Las contribuciones son bienvenidas. Puedes enviar un PR o reportar issues.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.

## Video explicativo
https://youtu.be/YsyqZ9g7rKU

