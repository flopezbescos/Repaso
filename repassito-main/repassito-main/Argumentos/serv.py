import socket,os,time
import threading


def server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    s.bind(('',16021))
    s.listen(1000)

    def worker(*args):
            nuevo_s= args[0]
            direccon=[args[1][0]]
            puerto= dir[1]

            opcion_cod=nuevo_s.recv(1024)
            opcion=opcion_cod.decode('utf8')
            print(opcion)
            if opcion=="Direccion":
                direccion="La direccion es " + direccon[0] #se concatena la direccion ip del cliente que se conecta a este servidor con el mensaje que se le va a enviar
                nuevo_s.send(direccion.encode('utf8'))
                print("Trabajo hecho!")

            if opcion=="Puerto":
                puerto_e="El puerto es " + str(puerto)
                nuevo_s.send(puerto_e.encode('utf8'))
                print("Trabajo hecho!")

            if not opcion =="Direccopm":
                if not opcion== "Puerto":
                    mensaje="\nERROR\n"
                    nuevo_s.send(mensaje.encode('utf8'))
                    print(mensaje)

            nuevo_s.close()

    while 1:
        nuevo_s,dir=s.accept()
        threading.Thread(target=worker, args=(nuevo_s,dir)).start() #se crea un hilo para cada cliente que se conecta al servidor y se le pasa como argumento el socket y la direccion ip del cliente que se conecta    

server()
