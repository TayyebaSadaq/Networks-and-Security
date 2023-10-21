import logging
import socket
import select

### SET UP LISTENING SOCKET ###
server_hostname = socket.gethostname() # change this to the server's hostname/IP address
server_port = 6060 # change this to the server's port number

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logging.info("Blocking - creating socket")

logging.info("Blocking - connecting")

s.connect((server_hostname, server_port))
logging.info("Blocking - connected")

logging.info("Blocking - sending...")
s.send(b"Hello, world!")

logging.info("Blocking - waiting...")
data = s.recv(1024)
logging.info(f"Blocking = data = {len(data)}")

logging.info("Blocking - closing socket")
s.close()