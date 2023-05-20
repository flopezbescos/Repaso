import socket

class ServidorTCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar_servidor(self):
        self.sock.bind((self.host, self.port))
        print(f'Servidor escuchando en {self.host}:{self.port}')
        self.sock.listen(1)

    def aceptar_conexion(self):
        conn, addr = self.sock.accept()
        print(f'Cliente conectado desde: {addr[0]}:{addr[1]}')
        self.conexion = conn

    def recibir_datos(self):
        data = self.conexion.recv(1024)
        print(f'Datos recibidos del cliente: {data.decode()}')

    def enviar_respuesta(self, response):
        self.conexion.sendall(response.encode())

    def cerrar_conexion(self):
        self.conexion.close()

    def cerrar_servidor(self):
        self.sock.close()


if __name__ == '__main__':
    servidor = ServidorTCP('localhost', 16041)
    servidor.iniciar_servidor()
    servidor.aceptar_conexion()
    servidor.recibir_datos()
    servidor.enviar_respuesta('¡Hola, cliente!')
    servidor.cerrar_conexion()
    servidor.cerrar_servidor()
