import socket
import threading
nombre_usuario = input("Dame el nombre de usuarios que deseas")
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("192.168.1.101", 9000))


def Reicibir():
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode("utf-8")

            if mensaje == "USUARIO":
                socket_cliente.send(nombre_usuario.encode("utf-8"))
            else:
                print(mensaje)

        except:
            print("A occurrido un error!")
            socket_cliente.close()
            break


def Escribir():
    while True:
        mensaje = (str(nombre_usuario) + ": " + input(""))
        socket_cliente.send(mensaje.encode("utf-8"))

hilo_recibir = threading.Thread(target=Reicibir)
hilo_enviar = threading.Thread(target=Escribir)

hilo_recibir.start()
hilo_enviar.start()