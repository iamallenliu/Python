import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '192.168.0.29'
PORT = 12341

s.bind((HOST, PORT))
s.listen(0)

print("Server started.")

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    data = data.decode("utf-8")

    if data == 'q':
        print("Connection terminated.")
        break
    else:
        print(data)

s.close()
