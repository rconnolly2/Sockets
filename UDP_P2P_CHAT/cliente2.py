import socket

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the IP address and port number to bind the socket to
server_address = ('192.168.1.101', 10001)
sock.bind(server_address)



# Receive messages
while True:
    try:
        mensaje = input("")
        sock.sendto(mensaje.encode("utf-8"), ("192.168.1.101", 10000))
        print("Tu: " + str(mensaje))
    except:
        sock.close()
        break

# Close the socket
sock.close()