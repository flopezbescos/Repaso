import socket, random, sys, signal, re
from sys import stderr

class Servidor:
    
    def initialize_connection(self):
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        direction = ('0.0.0.0', 16021)
        self.s_server.bind(direction)
        self.s_server.listen(5)
        print ("Server up!", file= stderr)

    def count_non_empty_lines(self):
        count = 0
        with open("frases.txt") as file_frases:
            for line in file_frases:
                if line.strip():  # Check if line is not empty after removing leading/trailing whitespace
                    count += 1
        return count
    
    def open_files(self):
        try:
            with open("fichero.txt") as archivo:
                frases = archivo.readlines()
        except FileNotFoundError:
            with open("frases.txt") as archivo:
                frases = self.count_frases(archivo)
        print(frases)
        return frases

    def count_frases(self, archivo):
        frases = []
        frase = ''
        for line in archivo:
            if line.startswith('Frase '):
                if frase:
                    frases.append(frase.strip())
                frase = line.lstrip('Frase ').rstrip('>>').strip()
            else:
                frase += line.strip()
        if frase:
            frases.append(frase.strip())
        return frases
    
    def recognize_frases(self):
        frases = self.open_files()
        return frases

    def accept(self):
            self.s_client, add = self.s_server.accept()
            print(f"Cliente conectado: {add}")

    def generate_frase(self, message):
        frases = self.recognize_frases()
        if message == "FRASE":
            # elegir un numero random random de frase y luego regresar esa frase
            frase_elegida = random.choice(frases).strip()
            return f"FRASE --> {frase_elegida}"
        elif message == "TOTAL":
            frase_total = len(frases)
            lineas = self.count_non_empty_lines()
            return f"TOTAL --> {frase_total} FRASES - {lineas} LINEAS"
        else: 
            return "ERROR --> Comando no soportado"
        
    def receive_message(self):
        message = self.s_client.recv(1024).decode("utf-8")
        return message
        
    def send_message(self, message):
        self.s_client.send(message.encode("utf-8"))
    
    def disconnect(self):
        self.s_client.close()
        print("Connection closed")
        sys.exit(0)

def signal_handler(signal, frame, server):
    print('\nTurning the server off', file=stderr)
    sys.exit(0)

if __name__ == '__main__':
    server = Servidor()
    signal.signal(signal.SIGINT, lambda signal, frame : signal_handler(signal, frame, server))   
    server.initialize_connection()
    while True:
        server.accept()
        message = server.receive_message()
        response = server.generate_frase(message)
        print(response, file=stderr)
        server.send_message(response)





                    
