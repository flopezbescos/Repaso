
import socket

class ClienteTCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        try:
            self.sock.connect((self.host, self.port))
            print(f'Conectado al servidor en {self.host}:{self.port}')
        except ConnectionRefusedError:
            print(f'No se puede establecer la conexión con el servidor en {self.host}:{self.port}')

    def enviar_mensaje(self, message):
        self.sock.sendall(message.encode())

    def recibir_respuesta(self):
        data = self.sock.recv(1024)
        print(f'Respuesta del servidor: {data.decode()}')

    def cerrar_conexion(self):
        self.sock.close()


if __name__ == '__main__':
    cliente = ClienteTCP('localhost', 16041)
    cliente.conectar()
    cliente.enviar_mensaje('Hola, servidor!')
    cliente.recibir_respuesta()
    cliente.cerrar_conexion()
