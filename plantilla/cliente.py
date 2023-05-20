import socket
import threading


class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def conectar(self):
        # Crear un socket TCP/IP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar al servidor
        self.client_socket.connect((self.host, self.port))

        # Iniciar un hilo para recibir respuestas del servidor
        response_thread = threading.Thread(target=self.receive_response)
        response_thread.start()

        while True:
            # Enviar comando al servidor
            command = input('Ingrese un comando: ')
            self.client_socket.sendall(command.encode())

    def receive_response(self):
        while True:
            # Recibir la respuesta del servidor
            response = self.client_socket.recv(1024).decode()
            print(f'Respuesta del servidor: {response}')


if __name__ == '__main__':
    # Crear instancia del cliente y conectar al servidor
    cliente = Cliente('localhost', 16041)
    cliente.conectar()
