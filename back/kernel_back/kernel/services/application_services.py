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
        self.service_state = self.start_service()


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

    def connect_to_service(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.service_host, self.service_port))
        return s