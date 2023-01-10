import socket
import threading
import rsa

#Creando key publica y privada
mi_key_pub, mi_key_priv = rsa.newkeys(1024)
su_key_pub = None # No sabemos su key publica
IPV4 = None # Esto es la variable IP que se utilizara o para hostear o para conectarse 

#Menu
opcion = int(input("Quieres ser host? pon 1 o cliente pon 2 "))
#Seleciona la IP
if opcion == 1:
    IPV4 = input("Dame tu IPV4 de esta maquina para hostear: ") #Eliges la ip que quieres utilizar para hostear
    #Haz ifconfig en linux para saber la ip de tu tarjeta de red o ipconfig en cmd en windows.
elif opcion == 2:
    IPV4 = input("Dame la IP de la maquina que te quieres conectar dentro de tu red: ")
    #Aqui pones la IP de la maquina que esta hosteando

if opcion == 1:
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((IPV4, 5000))

    socket_servidor.listen()

    cliente, _ = socket_servidor.accept()
    #Enviamos mi key publica al cuando el cliente se conecta a mi con en el estandar de llaves PKCS1 con formato PEM:
    cliente.send(mi_key_pub.save_pkcs1("PEM"))
    #Recibo la key publica del cliente para poder crear mensajes encriptados con rsa
    su_key_pub = rsa.PublicKey.load_pkcs1(cliente.recv(1024))
elif opcion == 2:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IPV4, 5000))
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
        print("El: " +  rsa.decrypt(client.recv(1024), mi_key_priv).decode("utf-8"))


hilo1 = threading.Thread(target=Enviar, args=(cliente,)) # Creamos hilo para enviar
hilo2 = threading.Thread(target=Recibir, args=(cliente,)) # Creamos hilo para recibir

hilo1.start()
hilo2.start()

