import socket
import threading


#gets host name 
print(socket.gethostname())
#gets the hosts IP from the host name
print(socket.gethostbyname(socket.gethostname()))
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5458
ADDR = (SERVER, PORT) #must be in a tuple

HEADER = 64
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "DISCONNECTED!"

#creats a socket to connect to using ipv4 address type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binds the server to this port and address and anything that will try to connect to this address will go to this socket
server.bind(ADDR) 
print(ADDR) 

def hundle_clint(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

# a loop that prints the messages betwin the server and clint
    connected = True
    while connected:
        #we make sure that the server will send a message in this case 64 bit message to the clint 
        #and will recive messages 
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECT!]{addr} {msg}")

 
                
            print(f"{addr} {msg}")
            conn.send("message received".encode(FORMAT))
    conn.close()    



def start():
    #will start the server to listen in the port
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #will wait for a new connection and store the info of the connection
        conn, addr = server.accept()
        #creates a new thread that will separate each connection
        thread = threading.Thread(target=hundle_clint, args=(conn, addr))
        #starts the thread
        thread.start()
        #will show how many active clint connections there are
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")


print(f"[STARTING] server {SERVER} is starting")
start()
