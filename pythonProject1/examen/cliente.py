import socket

class Cliente():
    def conexion(self):
        socketcliente= socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
        direction_destino=('127.0.0.1', 8888) #direccion salvo que te diga lo contrario es esa, puerto igual que el servidor
        socketcliente.connect(direction_destino)
        print("cliente activo")


if __name__ == '__main__':
    cliente= Cliente()
    cliente.conexion()

