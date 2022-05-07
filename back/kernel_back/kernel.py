import os
import sys
from ..gestor_archivos.initializer import start_service as start_archives
from ..gestor_aplicaciones.initializer import start_service as start_app

def initializer():
    if sys.argv[1] == '-start':
        os.system('python manage.py runserver')
        print("Iniciando Kernel...")
        start_app()
        print("Iniciando Gestor de Aplicaciones...")
        start_archives()
        print("Iniciando Gestor de Archivos...")
    elif sys.argv[1] == '-shutdown':
        shutdown()

def shutdown():
    pass