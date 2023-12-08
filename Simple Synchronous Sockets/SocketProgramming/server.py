import socket

#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the server to your hostname and port
s.bind((socket.gethostname(), 6060))
s.listen(5)

print("Server is up and listening for connections...")

while True:
    #accept the connection
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    
    #send welcome message to client
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    
    #close the connection
    clientsocket.close()
