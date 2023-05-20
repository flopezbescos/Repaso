import socket
import threading


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def iniciar(self):
        # Crear un socket TCP/IP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Vincular el socket a una dirección y puerto
        self.server_socket.bind((self.host, self.port))

        # Escuchar conexiones entrantes
        self.server_socket.listen(1)
        print(f'Servidor escuchando en el puerto {self.port}...')

        while True:
            # Aceptar una nueva conexión
            client_socket, address = self.server_socket.accept()
            print(f'Cliente conectado: {address[0]}:{address[1]}')

            # Manejar la conexión en un hilo separado
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            # Recibir comando del cliente
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # Calcular la respuesta (aquí puedes implementar la lógica necesaria)
            response = 'Respuesta del servidor: ' + data.upper()

            # Enviar la respuesta al cliente
            client_socket.sendall(response.encode())

        # Cerrar la conexión con el cliente
        client_socket.close()


if __name__ == '__main__':
    # Crear instancia del servidor y ejecutarlo en un hilo separado
    servidor = Servidor('localhost', 16041)
    server_thread = threading.Thread(target=servidor.iniciar)
    server_thread.start()
