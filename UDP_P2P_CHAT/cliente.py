import socket
import threading

def NuevoCliente(puerto_emisor, lista_puertos):
    #Esta funcion se llamara cuando detectemos un nuevo cliente habalando que no este
    #En nuestra lista
    for puerto in lista_puertos:
        if puerto_emisor == puerto:
            return True # Si el puerto enviado a la funcion esta dentro de nuestra lista de clientes conocidos devolvemos True
    else:
        return False # Si no es asi devolvemos falso

def Recibir(socket):
    while True:
        mensaje, direccion_emisor = socket.recvfrom(1024)
        ip_emisor, puerto_emisor = direccion_emisor
        # Miramos si el puerto del emisor ya lo conocemos:
        if NuevoCliente(puerto_emisor, lista_puertos_clientes) == False:
            lista_puertos_clientes.append(puerto_emisor) # Añadimos puerto a nuestra lista del cliente
            print("Añadiendo puerto: " + str(puerto_emisor) + " a nuestra lista")
            print(lista_puertos_clientes)
        mensaje = mensaje.decode("utf-8")
        print(str(direccion_emisor) + "Dice: " + mensaje)

    
opcion = input("Elige tu opcion:")


if opcion == "1":
    # Creando objeto socket
    socket_host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mipuerto = 10000
    miIP = "192.168.1.101"
    # Asignando mi ip y puerto al host
    direccion_server = (miIP, mipuerto)
    socket_host.bind(direccion_server)
    #Listas
    lista_puertos_clientes = []
    #Creo hilo para recibir mensajes y enviar:
    hilo_recibir = threading.Thread(target=Recibir, args=(socket_host,))
    #Empiezan hilos:
    hilo_recibir.start()

elif opcion == "2":
    # Creando objeto socket
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Asignando su ip y puerto
    supuerto = 10000
    suIP = "192.168.1.101"
    sudireccion_server = (suIP, supuerto)
    # Asignando mi ip y puerto
    mipuerto = 10001
    miIP = "192.168.1.101"
    midireccion_server = (miIP, mipuerto)
    socket_cliente.bind(midireccion_server)
    #Listas
    lista_puertos_clientes = []

    mensaje = str("Hola! " + str(supuerto))
    socket_cliente.sendto(mensaje.encode("utf-8"), sudireccion_server)
    print("Tu: " + str(mensaje))
else:
    #No a seleccionado o 1 o 2
    #Salimos del programa
    exit()




