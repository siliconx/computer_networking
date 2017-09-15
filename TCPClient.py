"""TCP client."""
from socket import socket, AF_INET, SOCK_STREAM
server_name = 'imcoder.xyz'
server_port = 12001
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
i = 0
while True:
    msg = 'I am a message, No.%d ' % i
    i += 1

    client_socket.send('a' * 1024)
    modified_msg = client_socket.recv(1024)
    print 'From server: ', modified_msg
client_socket.close()
