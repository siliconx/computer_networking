"""UDP server."""
from socket import socket, AF_INET, SOCK_DGRAM
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print 'The server is ready to receive'

while True:
    msg, client_address = server_socket.recvfrom(2048)
    print 'received message: %s' % msg
    modified_msg = msg.upper()
    server_socket.sendto(modified_msg, client_address)
