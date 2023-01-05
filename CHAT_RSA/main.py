import socket
import threading
import rsa

mi_key_pub, mi_key_priv = rsa.newkeys(1024)
su_key_pub = None

opcion = int(input("Quieres ser host? pon 1 o cliente pon 2"))

if opcion == 1:
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind(("192.168.1.101", 5000))

    socket_servidor.listen()

    cliente, _ = socket_servidor.accept()
    #Enviamos mi key publica al cuando el cliente se conecta a mi con en el estandar de llaves PKCS1 con formato PEM:
    cliente.send(mi_key_pub.save_pkcs1("PEM"))
    #Recibo la key publica del cliente para poder crear mensajes encriptados con rsa
    su_key_pub = rsa.PublicKey.load_pkcs1(cliente.recv(1024))
elif opcion == 2:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("192.168.1.101", 5000))
    #Recibimos primero la key publica del host
    su_key_pub = rsa.PublicKey.load_pkcs1(cliente.recv(1024))
    #Enviamos nuestra key publica al host en el estandar de llaves PKCS1 con formato PEM:
    cliente.send(mi_key_pub.save_pkcs1("PEM"))
else:
    exit()


def Enviar(client):
    while True:
        mensaje = input("")
        client.send(rsa.encrypt(mensaje.encode("utf-8"), su_key_pub))
        print("Yo: " + mensaje)
        

def Recibir(client):
    while True:
        print("El con IP:puerto: " + str(client.getpeername()) +  rsa.decrypt(client.recv(1024), mi_key_priv).decode("utf-8"))


hilo1 = threading.Thread(target=Enviar, args=(cliente,))
hilo2 = threading.Thread(target=Recibir, args=(cliente,))

hilo1.start()
hilo2.start()

