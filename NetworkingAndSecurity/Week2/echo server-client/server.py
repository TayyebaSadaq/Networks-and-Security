import socket

### set up listening socket
server_hostname = socket.gethostname() # change this to the server's hostname/IP address
server_port = 6060 # change this to the server's port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((server_hostname, server_port)) # bind socket to specific host/port
s.listen() # listen for connection to client

# accept connection from client
# [connection is a new socket object (send/receive data)]
# [address is internet address of client]
connection, address = s.accept() 


### Data is exchanged
with connection:
    print(f"Connected by {address}") # see where connection is coming from
    while True: # as long as client is sending data
        data = connection.recv(1024) # will take 1kb of data from client
        if not data: # if no data is received from client, break out of loop
            break