import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 6060)) # Connect to server

# Or simply omit this line as by default TCP sockets
# are in blocking mode

data = ("Hello Python\n", *10*1024*1024) # Huge amount of data to be sent
sock.send(data) # Send data till true