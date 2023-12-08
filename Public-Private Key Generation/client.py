import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

#Function to send requests to the server
def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.send(request.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

#Main entry point
if __name__ == "__main__":
    while True:
        #Get user command
        command = input("Enter command (REGISTER or GET): ").upper()

        if command == "REGISTER":
            #If the comman is REGISTER, get username and public key from the user
            username = input("Enter username: ")
            public_key = input("Enter public key: ")
            send_request(f"{command} {username} {public_key}")

        elif command == "GET":
            #If the comman is GET, get the username to retrieve the public key
            username = input("Enter username to retrieve public key: ")
            send_request(f"{command} {username}")

        else:
            #If the command is invalid, notify the user
            print("Invalid command. Please enter REGISTER or GET.")
