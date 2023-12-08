import selectors
import queue
import SMTPEncryption
from threading import Thread

class Module (Thread):
    def __init__(self, sock, addr):
        #intialize the module class a subclass of a thread
        Thread.__init__(self)

        self._selector = selectors.DefaultSelector() #create a selector for I/O multiplexing 
        self._sock = sock #stores the provided socket and address 
        self._addr = addr
        #creates thread-safe queues for incoming and outgoing data 
        self._incoming_buffer = queue.Queue()
        self._outgoing_buffer = queue.Queue()

        self.running = True #to indicate if the thread is running 
        self.encryption = SMTPEncryption.nws_encryption()
        events = selectors.EVENT_READ | selectors.EVENT_WRITE #define evetns for the socket 
        self._selector.register(self._sock, events, data=None) #register the socket with the selector for the specified events 

    def run(self):
        try:
            while self.running:
                #use selectors to wait for socket events 
                events = self._selector.select(timeout=1)
                for key, mask in events:
                    try: #checking for the read event and then calling it 
                        if mask & selectors.EVENT_READ:
                            self._read()
                        if mask & selectors.EVENT_WRITE and not self._outgoing_buffer.empty():
                            self._write() #check for write event and call the write method if there is outgoing data 
                    except Exception:
                        self.close() #any exception occurs close the connection 
                # Check for a socket being monitored to continue.
                if not self._selector.get_map():
                    break
        finally:
            self._selector.close() #close the selectoe when the loop exits 

    def _read(self):
        try: #attempt to receive data from the socket 
            data = self._sock.recv(4096)
        except BlockingIOError: 
            # Resource temporarily unavailable (errno EWOULDBLOCK)
            pass
        else:
            if data: #if data is received, decrypt it and put it into the incoming buffer
                self._incoming_buffer.put(self.encryption.decrypt(data.decode()))
            else:
                raise RuntimeError("Peer closed.") #if no data is received, raise a runtime error indicating that the peer closed the connection 

        self._process_response() #process the response 

    def _write(self):
        try: #attempt to get an outgoing message from the queue without waiting 
            message = self._outgoing_buffer.get_nowait()
        except:
            message = None

        if message:
            print("sending", repr(message), "to", self._addr)
            try:
                sent = self._sock.send(message)
            except BlockingIOError:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                pass

    def create_message(self, content):
        encoded = self.encryption.encrypt(content.encode()) #encrypt the content, encode it and put it into the outoging buffer
        self._outgoing_buffer.put(encoded)

    def _process_response(self):
        message = self._incoming_buffer.get() #get a message from the incoming buffer
        header_length = 3 #header length 
        if len(message) >= header_length:
             # Print the first three characters of the message as the header and the rest as the content
            print(message[0:header_length], message[header_length:])
        print("Processing thing")

    def _process_data_response(self):
        #process the accumulated data during the data transfer phase
        full_message = ''.join(self.data_buffer)
        print("Received data:", full_message)
        print("Exiting data phase...")
        self.data_buffer = [] #clear the data buffer

    def close(self):
        print("closing connection to", self._addr)

        self.running = False #tp stop the main loop in the run method 
        try:
            self._selector.unregister(self._sock)
            self._sock.close()
        except OSError as e: #ignore these specific errors 
            pass
        finally:
            # Delete reference to socket object for garbage collection
            self._sock = None


