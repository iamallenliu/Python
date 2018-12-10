import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = 'localhost'
PORT = 12341

s.bind((HOST, PORT))
s.listen(0)

print("Server started.")

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)

    if data == 'q':
        print("Connection terminated.")
        break
    else:
        print(data)

s.close()
