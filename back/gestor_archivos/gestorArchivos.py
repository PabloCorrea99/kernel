import socket
import os

class GestorArchivos:
    def __init__(self)-> None:
        self.estado = 1

    def start_service(self):
        print("Servicio Archivos Iniciado!")

def initializer():
    gestor = GestorArchivos()
    gestor.start_service()