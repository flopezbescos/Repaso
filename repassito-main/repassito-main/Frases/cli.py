import socket, time, pickle, select, sys, signal

class Cliente():

    def connection (self, destiny_direction=("127.0.0.1", 16021)):
        self.destiny_direction = destiny_direction
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.connect(self.destiny_direction)
        print("Client up!")
        print("Connection opened")


    def send_message(self, message):
        message = input("Introduce un comando: ")
        message_to_send = message.upper()
        # message = "FRASE"
        self.s.send(message_to_send.encode("utf-8"))

    def receive_message(self):
        respuesta = self.s.recv(1024).decode("utf-8")
        print(respuesta)

    def close_connection(self):
        self.s.close()
        print("Connection closed")

def signal_handler(signal, frame, server):
    print('\nClient down', file=sys.stderr)
    sys.exit(0)

if __name__ == '__main__':
    client = Cliente()
    client.connection()
    client.send_message("FRASE")
    client.receive_message()
    client.close_connection()
    
