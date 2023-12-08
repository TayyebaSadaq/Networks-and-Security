import socket
import threading
import json
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

#File paths
users_file = "users.json"
log_file = "server_log.txt"

#Function to load user data from file
def load_users():
    if os.path.exists(users_file):
        with open(users_file, 'r') as file:
            return json.load(file)
    return {}

#Function to save user data to file 
def save_users(users):
    with open(users_file, 'w') as file:
        json.dump(users, file, indent=2)

#Function to log requests to file 
def log_request(log_entry):
    with open(log_file, 'a') as file:
        file.write(log_entry + '\n')

#Function to generaate a unique user ID 
def generate_user_id():
    return str(len(load_users()) + 1)

#Function to handle client requests 
def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')

    if request.startswith("REGISTER"):
        _, username, public_key = request.split()
        users = load_users()

        if len(username) < 1:
            response = "FAIL REGISTER tooshort"
        elif username in users:
            response = "FAIL REGISTER inuse"
        else:
            user_id = generate_user_id()
            users[username] = {'id': user_id, 'key': public_key}
            save_users(users)
            response = f"SUCCESS REGISTER {username}"
            log_request(response)

    elif request.startswith("GET"):
        _, username = request.split()
        users = load_users()

        if username not in users:
            response = "FAIL GET nosuchid"
            log_request(response)
        else:
            public_key = users[username]['key']
            response = f"SUCCESS GET {username} {public_key}"
            log_request(response)

    else:
        response = "ERROR unknown"

    client_socket.send(response.encode('utf-8'))
    client_socket.close()

#Function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

#Main entry point
if __name__ == "__main__":
    start_server()
