import socket

HOST = "192.168.1.101"
PUERTO = 999

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_socket.connect((HOST, PUERTO))

cliente_socket.send("Hola mundo !".encode("utf-8"))

mensaje_recibido = cliente_socket.recv(1024)

print("El mensaje recibido por cliente es: " + mensaje_recibido.decode("utf-8"))

exit()