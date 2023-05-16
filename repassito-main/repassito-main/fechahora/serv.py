import sys, time, socket, select, signal
from sys import stderr

class Servidor:
    def initialize_connection(self):
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        direction = ('0.0.0.0', 16021)
        self.s_server.bind(direction)
        self.s_server.listen(5)
        print("Server up!", file=sys.stderr)

    def listen(self):
        while True:
            mensaje = self.receive()
            if not mensaje:
                break

    def accept(self):
        self.s_client, self.addr = self.s_server.accept()
        print("Connection opened from: ", self.addr, file=sys.stderr)

    def message_to_lower(self, mensaje):
        mensaje = mensaje.lower()
        return mensaje

    def receive(self):
        r_socket, __w_socket__, __e_socket__ = select.select([self.s_client], [], [])
        mensaje = r_socket[0].recv(1024).decode("utf-8")
        # mensaje = mensaje.lower()
        mensaje = self.message_to_lower(mensaje)
        if mensaje == "hora":
            self.enviar(self.hora())
        elif mensaje == "fecha":
            self.enviar(self.fecha())
        elif mensaje:
            self.enviar("ERROR")
        return  mensaje

    def enviar (self, mensaje):
        self.s_client.send(mensaje.encode("utf-8"))
        print("Sent:", mensaje, file=sys.stderr)

    def hora(self):
        self.mensaje = time.strftime("%H:%M:%S")
        return self.mensaje
    
    def fecha(self):
        self.mensaje = time.strftime("%d/%m/%Y")
        return self.mensaje

    def disconnect(self):
        print("Closing connection from", self.addr, file=sys.stderr)
        self.s_client.close()

def signal_handler(signal, frame, server):
    print('\nTurning the server off', file= stderr)
    sys.exit(0)


if __name__ == "__main__":
    server = Servidor()
    signal.signal(signal.SIGINT, lambda signal, frame : signal_handler(signal, frame, server))   
    server.initialize_connection()
    while True:
        server.accept()
        mensaje = server.listen()

