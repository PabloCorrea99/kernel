import socket
import os
from pathlib import Path
# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8002
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
NODOS_DIR = Path(__file__).resolve()

def startSockets():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(4)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept() 

    print(f"[+] {address} is connected.")

    received = client_socket.recv(BUFFER_SIZE).decode()
    msg = received.split(SEPARATOR)
    if msg[0] == "start":
        print("[+] Service started")
        send_message(client_socket)
    elif msg[0] == "EXIT":
        exit(0)

    s.close()

def send_message(client_socket):
    status = b'1'
    client_socket.sendall(status)

def startServer():   
    while True:
        startSockets()

startServer()