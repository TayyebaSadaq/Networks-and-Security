import socket
import threading #used to handle multiple clients

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDRESS = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        message = connection.recv(SIZE).decode(FORMAT)
        if message == DISCONNECT_MESSAGE:
            connected = False
        
        print(f"[{address}] {message}")
        message = f"message received: {message}"
        connection.send(message.encode(FORMAT))
    
    connection.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen() 
    print(f"[LISTENING] Server is listening on {IP}")

    while True:
        connection, address = server.accept() #accepts incoming connections
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    main()