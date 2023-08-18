import socket

server_ip = '127.0.0.1'
server_port = 9090
size = 1024
server_addr = (server_ip, server_port)

#set client's socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_addr)
    while True:
        data = input("message : ")
        if not data:
            break
# str to bytearray : bytearray(STR, 'utf-8') : STR을 입력한 인코딩 방식으로 bytearray 타입으로 변환합니다.
# bytearray to str : BYTES.encode('utf-8') or str.encode(BYTES, 'utf-8') : BYTES을 입력한 인코딩 방식의 str 타입으로 변환합니다.
        client_socket.send(str.encode(data))
        msg = client_socket.recv(size)
        if not msg:
            break
        print("resp from server : {}".format(msg))