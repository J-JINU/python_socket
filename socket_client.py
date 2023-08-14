import socket

server_ip = '127.0.0.1'
server_port = 1234
size = 1024
server_addr = (server_ip, server_port)

#set client's socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_addr)
    client_socket.send("hi".encode())
    msg = client_socket.recv(size)
    print("resp from server : {}".format(msg))