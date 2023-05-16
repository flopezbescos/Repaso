import socket, time, pickle, select, sys, signal
from sys import stderr

class Cliente():

    def initialize (self, destiny_direction=("127.0.0.1", 16021)):
        self.destiny_direction = destiny_direction
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.connect(self.destiny_direction)
        print("Client up!")
        print("Connection opened")

    def ask_for_petition(self):
        petition = input("Se chequeara si la frase o el numero es palindromo: ")
        return petition
    
    def send_petition(self, petition):
        if petition == "Frase":
            word = input("Ingrese la frase que quiere chequear: ")
            self.s.send(b"Frase")
            self.s.send(word.encode("utf-8"))
            print("Sent:", word)
        elif petition == "Numero":
            number = input("Ingrese el numero que quiere chequear: ")
            self.s.send(b"Numero")
            self.s.send(number.encode("utf-8"))
            print("Sent:", number)
        else:
            print("No se ingreso una opcion valida, se cerrara el cliente con ctrl+c")
            signal.signal(signal.SIGINT, self.signal_handler)

    def receive_answer(self):
        data = self.s.recv(1024)
        print("Received:", data.decode("utf-8"))

    def disconnect(self):
        self.s.close()
        print("Connection closed")

    def signal_handler(signal, frame, server):
        print('\nTurning the client off', file=stderr)
        sys.exit(0)


if __name__ == "__main__":
    client = Cliente()
    client.initialize()
    petition = client.ask_for_petition()
    client.send_petition(petition)
    client.receive_answer()
    client.disconnect()
        
