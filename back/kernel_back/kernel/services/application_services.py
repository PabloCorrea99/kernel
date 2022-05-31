import socket
import os
from pathlib import Path

# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 80
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

class Application_Service:
    def __init__(self, operation) -> None:
        self.service_port = 8002
        self.service_host = "127.0.0.1"
        self.method = operation
        if operation == 'start':
            self.service_state = self.start_service()
        elif operation == 'exit':
            self.service_state = self.stop_service()



    def start_service(self):
        method = 'start'
        print(f"[+] Connecting to {self.service_host}:{self.service_port}")
        s = self.connect_to_service()
        print("[+] Connected.")
        s.send(f"{method}{SEPARATOR}".encode())
        state = 0
        while True:
            # read the bytes from the file
            bytes_read = s.recv(BUFFER_SIZE)
            print('BYTES ',bytes_read)
            if not bytes_read:
                # file transmitting is done
                break
            state = int(bytes_read)
        s.close()
        if state == 1:
            print("[+] Application Service Started")
        else:
            print("[-] Oops we couldn't start the service")
        return int(state)

    def manage_app(self, id):
        s = self.connect_to_service()
        s.send(f"{self.method}{SEPARATOR}".encode())
        response = b''
        while True:
            # read the bytes from the file
            bytes_read = s.recv(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            else:
                response += bytes_read 
        s.close()
        return response
    
    def stop_service(self):
        s = self.connect_to_service()
        s.send(f"{self.method}{SEPARATOR}".encode())
        state = 1
        while True:
            # read the bytes from the file
            bytes_read = s.recv(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            state = int(bytes_read)
            if state == 0:
                break
        s.close()
        if state == 0:
            print("[+] Application Service Stopped")
        else:
            print("[-] Oops we couldn't stop the service")
        return state

    def connect_to_service(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.service_host, self.service_port))
        return s