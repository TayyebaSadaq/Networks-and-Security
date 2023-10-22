import sys
import socket
import selectors
import types

### ACCEPT CONNECTIONS ###    
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE # Register the new connection for READ and WRITE events
    sel.register(conn, events, data=data)

### SERVICE CONNECTIONS ###
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data: # check if data is empty
            data.outb += recv_data
        else: # no data means connection is closed
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:] # discard the sent data

sel = selectors.DefaultSelector()

### SET UP LISTENING SOCKET ###

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False) # Set to non-blocking mode
sel.register(lsock, selectors.EVENT_READ, data=None) # Register the socket to be monitored with sel.register()
# data is used to store whatever arbitrary data you’d like along with the socket.#

### EVENT LOOP ###
try:
    while True:
        events = sel.select(timeout=None) # blocks until there are sockets ready for I/O
        for key, mask in events:
            if key.data is None: # If the key.data attribute is None, we know it’s from listening socket and need to accept() connection.
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()

