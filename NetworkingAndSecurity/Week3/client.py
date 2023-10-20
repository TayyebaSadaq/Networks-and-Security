import socket
import threading #used to handle multiple clients

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDRESS = (IP,PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    print(f"[CONNECTED] Client connected to {IP}")

    connected = True
    while connected:
        message = input(">")

        client.send(message.encode(FORMAT))
        if message == DISCONNECT_MESSAGE:
            connected = False
        else:
            message = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {message}")

if __name__ == "__main__":
    main()