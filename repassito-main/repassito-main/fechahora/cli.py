import socket, signal, os, sys
from sys import stderr

class Cliente:
    def __init__(self):
        ip = "localhost"
        puerto = 16000+20+1
        self.direccion = (ip, puerto)
        self.s = None

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s.connect(self.direccion)

    def send(self, mensaje):
        self.s.send(mensaje.encode("utf-8"))

    def receive(self):
        return self.s.recv(1024).decode("utf-8")
    
    
def signal_handler(signal, frame, server):
    print('\nClient down', file=sys.stderr)
    sys.exit(0)
    

if __name__ == "__main__":
    client = Cliente()
    signal.signal(signal.SIGINT, lambda signal, frame : signal_handler(signal, frame, client))
    client.connect()
    while True:
        mensaje = input("Write the message: ")
        client.send(mensaje)
        print(client.receive())
        
