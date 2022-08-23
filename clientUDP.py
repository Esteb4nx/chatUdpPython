import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 33333

print("Server IP: %s" % SERVER_IP)
print("Server port: %s" % SERVER_PORT)

cliente = input("Ingresa tu nombre: ")
while True:
    msg = input(cliente+": >> ")

    msg = msg.encode('UTF-8')
    # print("Mensaje: %s" % msg.decode('UTF-8'))

    sock = socket.socket(socket.AF_INET, # IPv4
                        socket.SOCK_DGRAM) # Protocolo UDP

    sock.sendto(msg, (SERVER_IP, SERVER_PORT))