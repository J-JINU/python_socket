import socket

ip = ''
port = 9090
size = 1024
addr = (ip, port)

#set server's socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(addr)
    server_socket.listen()
    while True:
        client_socket, client_addr = server_socket.accept()
        while True:
            msg = client_socket.recv(size)
            if not msg:
                break
            print("[{}] massage : {}".format(client_addr, msg))
            client_socket.sendall(msg)
        client_socket.close()