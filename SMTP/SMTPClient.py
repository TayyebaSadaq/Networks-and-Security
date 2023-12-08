__author__ = "Christopher Windmill, Brad Solomon" #specifies the author of the code and rhe code is attributed towards the specfic name
__version__ = "1.0.1" #specfies the version numbers of the code and these are often used to track changes and updates to the codebase 
__status__ = "Development" #the status is set to "development", this means it is still under development and it can be changed to production or stable 

import socket
import selectors
import threading
import SMTPClientLib

class NWSThreadedClient ():
    def __init__(self, host="127.0.0.1", port=12345):
        #this initializes various attributes such as the network components
        if __debug__:
            print("NWSThreadedClient.__init__", host, port)

        # Network components
        self._host = host
        self._port = port
        self._listening_socket = None
        self._selector = selectors.DefaultSelector() #default selector for I/O multiplexing 

        self._module = None

    def start_connection(self, host, port):
        addr = (host, port)
        print("starting connection to", addr)

#create a non blocking socket 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        #initiate a non blocking connection to the server 
        sock.connect_ex(addr)

        self._module = SMTPClientLib.Module(sock, addr) #this creates an instance of the SMTPClientLib.Module
        self._module.start()
        #start the module in a seperate thread 
    
    def helo(self, domain):
        self._module.send_message(f'HELO {domain}')

    def mail_from(self, sender):
        self.module.send_message(f'MAIL FROM: {sender}')
    
    def rcpt_to(self, recipient):
        self._module.send_message(f'RCPT TO: {recipient}')
    
    def quit_session(self):
        self._module.send_message('QUIT')

    def run(self):
        self.start_connection(self._host, self._port)
        #starts a connection to the specifies host and port 

        while True: #loops to continuously get user input and create mesages
            useraction = input("Enter a string")
            if useraction.upper() == 'HELO':
                domain = input("Enter your domain: ")
                self.helo(domain)
            elif useraction.upper() == 'MAIL FROM':
                sender = input("Enter sender email address: ")
                self.mail_from(sender)
            elif useraction.upper() == 'RCPT TO':
                recipient = input("Enter recipient email address: ")
                self.rcpt_to(recipient)
            elif useraction.upper() == 'QUIT':
                self.quit_session()
                break 
            else:
                self._module.create_message(useraction)


if __name__ == "__main__":
    client = NWSThreadedClient() #create an instnace of NWSThreadedClient and run the client 
    client.run()