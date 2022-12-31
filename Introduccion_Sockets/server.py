import socket

HOST = "192.168.1.101"
PUERTO = 999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PUERTO))

server.listen(5)

while True:
    socket_comunicacion, direccion = server.accept()
    print("Connectado ! a " + str(direccion))

    mensaje = socket_comunicacion.recv(1024).decode("utf-8")
    print("Mensaje es: " + mensaje)

    socket_comunicacion.send("Tengo tu mensaje, gracias !".encode("utf-8"))
    socket_comunicacion.close() #Cerramos comunicacion
    print("Cerrando comunicacion")