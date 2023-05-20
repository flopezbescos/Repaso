import socket

class Cliente:
    def __init__(self, host='localhost', port=10641):
        self.host = host
        self.port = port

    def enviar_frase(self, frase):
        try:
            # Conectarse al servidor
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
                cliente_socket.connect((self.host, self.port))

                # Enviar la frase al servidor
                cliente_socket.sendall(frase.encode())

                # Recibir la respuesta del servidor
                respuesta = cliente_socket.recv(1024).decode()
                print(respuesta)
        except ConnectionRefusedError:
            print("No se puede establecer una conexión con el servidor.")

# Crear una instancia del cliente y enviar una frase
cliente = Cliente()
frase = input("Ingrese una frase: ")
cliente.enviar_frase(frase)
