import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reuse port connection due to delay
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
HOST = '192.168.0.29'
PORT = 12341
s.bind((HOST, PORT))
s.listen(0)
print("Server started.")

# Accept client connection.
conn, addr = s.accept()

msg = 'Connection to host: ' + HOST
msg = bytes(msg, 'utf-8')

print('Connected by', addr)

# Send authenication.
conn.sendall(msg)

while True:
    data = conn.recv(1024)
    data = data.decode("utf-8")

    if data == 'q':
        print("Connection terminated.")
        break
    else:
        print(data)

s.close()
