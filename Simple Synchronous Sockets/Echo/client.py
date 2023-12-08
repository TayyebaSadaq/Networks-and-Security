import socket

### CLIENT INITIATING CONNECTION ###
#define server's hostname and port
server_hostname = socket.gethostname() #change this to the server's hostname/IP address
server_port = 6060 #change this to the server's port number


# create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_hostname, server_port)) # connect to the server [PAUSES HERE TILL CONNECTION ESTABLISHED]

### EXCHANGE DATA ###

client_socket.sendall(b"Hello, world") # send data [b = 8bits]
data = client_socket.recv(1024)

print(f"Received: {data}")
