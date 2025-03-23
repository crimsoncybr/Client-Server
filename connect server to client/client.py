import socket
import time

PORT = 5458
HEADER = 64
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "DISCONNECTED!"
SERVER = "192.168.1.122" 
ADDR = (SERVER, PORT)

Clint =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Clint.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length  += b' ' *(HEADER - len(send_length))
    Clint.send(send_length)
    Clint.send(message)
    print(Clint.recv(2048).decode(FORMAT))

send("hello world")
send(DISCONNECT_MESSAGE)