import os, socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

nombre_server=input("Nombre del servidor: \n")
ip=socket.gethostbyname(nombre_server)
puerto=input("Introduzca un puerto: \n")
dir=(ip,int(puerto))
s.connect(dir)

opcion_decod=input("1.Direccion \n2.Puerto \nIntroduzca una opcion:")

opcion=opcion_decod.encode('utf8')
s.send(opcion)

respuesta=s.recv(1024)
os.write(2,respuesta)

s.close()