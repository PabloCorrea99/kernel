import socket
import os
from pathlib import Path
import json
# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
DIR = os.path.join(Path(__file__).resolve().parent, 'directorio')

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
    elif msg[0] == "create":
        create_directory(msg[1], client_socket)
    elif msg[0] == "delete":
        delete_directory(msg[1], client_socket)
    elif msg[0] == "exit":
        exit_service(client_socket)

    s.close()

def send_message(client_socket):
    status = b'1'
    client_socket.sendall(status)

def create_directory(name, client_socket):
    data = {}
    try:
        path = os.path.join(DIR, name)
        os.mkdir(path)
        data = json.dumps({'status':1, 'result':name})
    except Exception as e:
        data = json.dumps({'status':0, 'result':str(e)})
    print(data)
    client_socket.sendall(data.encode())

def delete_directory(name, client_socket):
    data = {}
    try:
        path = os.path.join(DIR, name)
        os.rmdir(path)
        data = json.dumps({'status':1, 'result':name})
    except Exception as e:
        data = json.dumps({'status':0, 'result':str(e)})
    print(data)
    client_socket.sendall(data.encode())

def exit_service(client_socket):
    data = b'0'
    client_socket.sendall(data)
    print("[+] Service stopped")
    client_socket.close()
    exit(0)

    
    
def startServer():   
    while True:
        startSockets()

startServer()