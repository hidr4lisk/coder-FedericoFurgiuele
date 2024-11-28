
# Instalar UV -
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Iniciar el proyecto en UV
    uv init 
# Creación del Entorno Virtual
    uv venv
# Agregando Django
    uv add django
# Creación carpeta SRC
    mkdir src
# Iniciamos proyecto en Django
    PROYECTO/src/django-admin startproject config .
# Ejecutamos servidor Django
    PROYECTO/src/python manage.py runserver
# Configuramos en Español

# Creamos aplicación Django
    PROYECTO/src/python manage.py startapp core

# Si cambiamos de pc
    podemos clonar y usar UV SYNC

# Cambiamos el Idioma
    proyecto/src/config/setttings.py linea 106

# Apenas creamos una aplicación la REGISTRAMOS
    proyecto/src/config/setttings.py  linea 33 INSTALLED_APPS, sobre el final

# Nuestro Primer controlador
    en coder-federicofurgiuele\src\core>views.py

    from django.http import HttpResponse _ Arriba de todo
    
    y la funcion 
    
    def saludar(request):
        return HttpResponse("Hola desde Django!")

    Luego le damos una puerta "URL"

    coder-federicofurgiuele\src\core>urls.py
    from core import views

    urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/")
    ]

# Plantillas de Django
    dentro del servidor, SRC/CORE creamos la carpeta "templates"
    luego ingresamos a esa carpeta y creamos otra carpeta con el nombre de la APP

# Creamos un HTML en templates/core
    creamos index.html

# Nueva funcion en views

    def index(request):
     return render(request, "core/index.html")

# a esa función que genera el HTML, le podemos pasar variables

    def index(request):
     context={"año: 2024"}
     return render(request, "core/index.html", context)

# ahora en el index.html podemos usar esa variable Año
        <footer>Hecho en el año {{año}}</footer>