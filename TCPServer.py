"""TCP server."""
from socket import socket, AF_INET, SOCK_STREAM
server_port = 12001
max_connections = 9
# welcome socket, to create connection socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(max_connections)
print 'The server is ready to receive...'
connection_socket, address = server_socket.accept()

while True:
    msg = connection_socket.recv(1024)
    upper_msg = msg.upper()
    connection_socket.send(upper_msg)

connection_socket.close()
