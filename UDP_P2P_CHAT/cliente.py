import socket

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the IP address and port number to bind the socket to
server_address = ('192.168.1.101', 10000)
sock.bind(server_address)

# Receive messages
while True:
    try:
        data, address = sock.recvfrom(4096)
        print(f'Received message from {address}:' + data.decode("utf-8"))
    except:
        sock.close()
        break

