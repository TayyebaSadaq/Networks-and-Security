__author__ = "Christopher Windmill, Brad Solomon"

__version__ = "1.0.1"
__status__ = "Development"

import socket
import selectors
import SMTPServerLib

class NWSThreadedServer():
    def __init__(self, host="127.0.0.1", port=12345):
        if __debug__:
            print("NWSThreadedServer.__init__", host, port)

        # Network components
        self._host = host
        self._port = port
        self._listening_socket = None
        self._selector = selectors.DefaultSelector()

        # Processing Components
        self._modules = []

    def _configureServer(self):
        self._listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a listening socket, configure it and register it with the selector 
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        self._listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._listening_socket.bind((self._host, self._port))
        self._listening_socket.listen()

        print("listening on", (self._host, self._port))
        self._listening_socket.setblocking(False)
        self._selector.register(self._listening_socket, selectors.EVENT_READ, data=None)

    def accept_wrapper(self, sock):# Accept a connection, configure the new socket, and start a new module for communication
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)

        conn.setblocking(False)
        module = SMTPServerLib.Module(conn, addr)# Assuming SMTPServerLib is imported and Module class is defined
        self._modules.append(module)
        module.start()

    def run(self):
         # Configure the server and enter the main loop to handle events
        self._configureServer()

        try:
            while True:
                events = self._selector.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        # If the data is None, it's the listening socket, so accept a new connection
                        self.accept_wrapper(key.fileobj)
                    else:
                       # Handle other events (not implemented in this commented version)
                       pass
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            self._selector.close() #close the selector 


if __name__ == "__main__":
    # Create an instance of NWSThreadedServer and run the server
    server = NWSThreadedServer()
    server.run()