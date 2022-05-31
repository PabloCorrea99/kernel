import socket
import os
from pathlib import Path
import subprocess
import random
import json
# device's IP address
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8002
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
NODOS_DIR = Path(__file__).resolve()
pid_array = []

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
    elif msg[0] == "run":
        run_app(client_socket)
    elif msg[0] == "stop":
        stop_app(client_socket)
    elif msg[0] == "exit":
        exit_service(client_socket)

    s.close()

def send_message(client_socket):
    status = b'1'
    client_socket.sendall(status)

def run_app(client_socket):
    data = {}
    try:
        cp = subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        pid_array.append(cp.pid)
        data = json.dumps({'status':1, 'result':cp.pid})
    except Exception as e:
        data = json.dumps({'status':0, 'result':str(e)})
    client_socket.sendall(data.encode())
        
        
def stop_app(client_socket):
    data = {}
    try:
        process = random.choice(pid_array)
        os.system(f'TASKKILL /PID {process}')
        pid_array.remove(process)
        data = json.dumps({'status':1, 'result':process})
    except Exception as e:
        data = json.dumps({'status':0, 'result':str(e)})
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