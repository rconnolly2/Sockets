import socket
import threading
import random

class Cliente():
    def __init__(self, mi_nombre_usuario):
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Permitir utilizar la misma direccion socket
        self.mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mi_ip = "127.0.0.1"
        self.mi_puerto = 5026
        self.mi_nombre_usuario = mi_nombre_usuario

        self.mi_socket.bind((self.mi_ip, self.mi_puerto)) # Seleccionamos nuestra ip y puerto para poder escuchar
        self.mi_socket.listen(5)
        print("Cliente iniciado con ip: " + str(self.mi_ip) + ":" + str(self.mi_puerto))

        #Listas de datos:
        self.lista_sockets_clientes = []
        self.lista_usuarios = []
        self.lista_puertos = []


    def Aceptar_Sesiones(self):
        while True:
            su_socket_cliente, su_ip_puerto = self.mi_socket.accept()
            su_ip, su_puerto = su_ip_puerto

            su_nombre_usuario = su_socket_cliente.recv(1024).decode("utf-8")
            su_socket_cliente.send(self.mi_nombre_usuario.encode("utf-8"))
            #Añadimos datos a nuestras listas:
            self.lista_sockets_clientes.append(su_socket_cliente)
            self.lista_usuarios.append(su_nombre_usuario)
            self.lista_puertos.append(su_puerto)

            hilo_enviar = threading.Thread(target=self.Mensaje_Broadcast, args=(su_socket_cliente,))
            hilo_recibir = threading.Thread(target=self.Recibir_Mensajes, args=(su_socket_cliente,))

    def Recibir_Mensajes(self, cliente):
        while True:
            try:
                mensaje = cliente.recv(1024).decode("utf-8")
                print("Ellos: " + mensaje)
            except:
                print("conexion rota!")

    
    def Mensaje_Broadcast(self, cliente):
        while True:
            mensaje = input("")
            for cliente in self.lista_sockets_clientes:
                cliente.send((self.lista_usuarios[self.lista_sockets_clientes.index(cliente)] + mensaje).encode("utf-8"))
                print("Yo: " + mensaje)


    
if __name__ == "__main__": #Solo ejecutar esta parte si especificamente se ejecuta este archivo .py
                            #Si se importa esta clase a otro archivo esto NO SE EJECUTARA
    cliente1 = Cliente("robert")
    cliente1.Aceptar_Sesiones()

