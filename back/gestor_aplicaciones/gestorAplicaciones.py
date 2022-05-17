import socket
import os

class GestorAplicaciones:
    def __init__(self)-> None:
        self.estado = 1

    def start_service(self):
        print("Servicio Aplicaciones Iniciado!")

def initializer():
    gestor = GestorAplicaciones()
    gestor.start_service()

initializer()