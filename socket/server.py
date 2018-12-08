import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port

name = "allen"


s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   print 'allen liu'
   c.send('Thank you for connecting')
   c.close()
