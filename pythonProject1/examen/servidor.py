import socket #siempre

class Server():

    def conexion(self):
        while True:
            socketserver= socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
            #SI ES UDP: socketserver= socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
            #SI ES UDM(LOCAL): socketserver= socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
            direction=('0.0.0.0', 8888) #numero que yo quiera siempre mayor que 4000
            socketserver.bind(direction)
            socketserver.listen(5) #siempre 5 salvo que el enunciado te diga lo contrario.
            socketclient, adr =socketserver.accept()

            print("Servidor activo")


if __name__ == '__main__':
    server= Server()
    server.conexion()

