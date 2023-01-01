import socket
import threading

HOST = "192.168.1.101"
PUERTO = 9000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((HOST, PUERTO)) #Asignamos direccion y puerto de nuestro servidor

socket_server.listen(5)

clientes = []
nombres_usuarios = []

def Broadcast(mensaje):
    for cliente in clientes:
        cliente.send(mensaje) #Enviara un mensaje a cada cliente. Broadcast => Lo escuchan todos


def Manejar_Conexion(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            Broadcast(mensaje)
        except:
            index_cliente = clientes.index(cliente) # Cojemos el index de la lista clientes
            clientes.remove(cliente)
            cliente.close()
            nombre_usuario = nombres_usuarios[index_cliente]
            Broadcast((str(nombre_usuario) + " abandono el chat").encode("utf-8"))
            nombres_usuarios.remove(nombre_usuario)
            break

def Recibir():
    while True:
        cliente, direccion = socket_server.accept()
        print("Conectado con direccion: " + str(direccion))

        cliente.send("USUARIO".encode("utf-8"))
        nombre_usuario = cliente.recv(1024).decode("utf-8")
        nombres_usuarios.append(nombre_usuario)
        clientes.append(cliente)

        print("Hemos añadido nombre usuario: " + str(nombre_usuario))
        Broadcast(("Nombre de usuario añadido al chat : " + str(nombre_usuario)).encode("utf-8"))
        cliente.send("Conectado al servidor !".encode("utf-8"))

        hilo = threading.Thread(target=Manejar_Conexion, args=(cliente,))
        hilo.start()

print("Servidor esta escuchando!")
Recibir()