from cliente import Cliente
import socket
import threading

class Cliente2(Cliente):
    def __init__(self, mi_nombre_usuario):
        super().__init__(mi_nombre_usuario)
        self.mi_puerto = 5004

    def Conectar(self):
        self.mi_socket.connect(("127.0.0.1", self.mi_puerto))
        self.mi_socket.send(self.mi_nombre_usuario.encode("utf-8"))



cliente2 = Cliente2("pedro")
cliente2.Conectar()
cliente2.Aceptar_Sesiones()


