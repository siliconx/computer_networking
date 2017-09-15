"""UDP clinet."""
from socket import socket, AF_INET, SOCK_DGRAM
server_name = 'imcoder.xyz'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
i = 0
while True:
    message = 'Input lowercase sentence: No.%d' % i
    i += 1

    client_socket.sendto(message, (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print modified_message
client_socket.close()
