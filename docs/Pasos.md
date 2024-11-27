# Instalar UV -
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Iniciar el proyecto en UV
    uv init 
# Creación del Entorno Virtual
    uv venv
# Agregamos Django
    uv add django
# 