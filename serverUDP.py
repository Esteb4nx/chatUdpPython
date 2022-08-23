import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 33333

sock = socket.socket(socket.AF_INET, # IPv4
                     socket.SOCK_DGRAM) # Protocolo UDP

sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr = sock.recvfrom(1024) #Tamaño Buffer
    print("Mensaje de %s: %s"% (addr[0],data.decode('UTF-8')))