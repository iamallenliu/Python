import socket

HOST = 'localhost'
PORT = 12341

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Chat client started.")
print("Enter 'q' to quit")

while True:

    mystring = input("Type your message: ")
    b = bytes(mystring, 'utf-8')
    s.sendall(b)

    if mystring == 'q':
        print("Connection terminated.")
        break

s.close()
