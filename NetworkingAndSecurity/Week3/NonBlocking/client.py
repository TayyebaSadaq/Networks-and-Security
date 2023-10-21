import socket

#create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define server's hostname and port
server_hostname = socket.gethostname() #change this to the server's hostname/IP address
server_port = 6060 #change this to the server's port number

#connect to the server
s.connect((server_hostname, server_port))

#receive message from server
message = s.recv(2848)

#close socket when done
s.close()

#print received message
print(f"Message Received: {message.decode('utf-8')}") #decode the message from bytes to string
