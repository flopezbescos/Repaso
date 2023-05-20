import socket

class Servidor:
    def __init__(self, host='localhost', port=10641):
        self.host = host
        self.port = port

    def iniciar(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_socket:
                servidor_socket.bind((self.host, self.port))
                servidor_socket.listen(1)

                print(f"Servidor escuchando en {self.host}:{self.port}")

                while True:
                    cliente_socket, cliente_addr = servidor_socket.accept()
                    print(f"Cliente conectado desde {cliente_addr[0]}:{cliente_addr[1]}")

                    frase = self.recibir_frase(cliente_socket)
                    respuesta = self.check(frase)
                    self.enviar_respuesta(cliente_socket, respuesta)

                    cliente_socket.close()

        except OSError:
            print("Error al iniciar el servidor.")

    def recibir_frase(self, cliente_socket):
        frase = cliente_socket.recv(1024).decode()
        return frase

    def check(self, frase):
        if self.es_palindroma(frase):
            return "Es palindroma"
        else:
            return "No es palindroma"
    def es_palindroma(self, frase):
        frase = frase.replace(" ", "").lower()
        if frase == frase[::-1]:
            return True
        else:
            return False

    def enviar_respuesta(self, cliente_socket, respuesta):
        cliente_socket.sendall(respuesta.encode())

# Crear una instancia del servidor y empezar a escuchar
servidor = Servidor()
servidor.iniciar()
