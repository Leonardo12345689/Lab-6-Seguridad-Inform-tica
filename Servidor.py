#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:35:10 2022

@author: carlofaundez
"""

import socket



#Funcion para calcular d verificando congruencia de e y fi de n
def calcula_d(e,fi_n):
	k=1
	m=(1+(k)*(fi_n))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(fi_n))%(e)
	d=int((1+(k)*(fi_n))/(e))
	return d




#############################Descifrado##############################################

#Funcion para descifrar mensaje
def descifrar_mensaje(msj,key):
	msj=msj.upper()
	lm=msj.split("  ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=descifrar_numero(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc


#Funcion para descifrar palabra, esta funcion es usada por la que descifra el mensaje
def descifrar_numero(m,k):
    
    lnc=[]
    ln=[]
    n,d=k
    cnc=""
    men=m.split(" ")
    for i in men:
        x=int(i)
        ln.append(x)
        print(x)
    for j in ln:
        m=(j**d)%n
        lnc.append(m)
    for k in lnc:
        l=buscarlet(k)
        cnc=cnc+str(l)
        
    return cnc


#Funcion para encontrar la posicion de un numero en el abecedario, entregando la letra
def buscarlet(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1	





def server():
    host = "127.0.0.1" #Asignar ip
    port = 1234 #Asignar puerto

    server_socket = socket.socket()  #Obtener la instancia
    server_socket.bind((host, port))  #junta la ip con el puerto

    server_socket.listen(1) #Definir cuantos clientes pudo tener conectados
    conn, address = server_socket.accept()  #Para aceptar nuevas conexiones
    print("Connection from: " + str(address))

    #Recivir P
    p = int(conn.recv(1024).decode())
    if not p:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("p es: " + str(p))

    #Enviar temp
    temp=0
    conn.send(str(temp).encode())  #envio de paquete a cliente


    #Recivir q
    q = int(conn.recv(1024).decode())
    if not q:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("q es: " + str(q))


    #Enviar tem2
    temp2=0
    conn.send(str(temp2).encode())  #envio de paquete a cliente

    #Recivir n
    n = conn.recv(1024).decode()
    if not n:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("n es: " + str(n))
    
    #Enviar tem3
    temp3=0
    conn.send(str(temp3).encode())  #envio de paquete a cliente 
    
    #Recivir fi de n
    fi_n = conn.recv(1024).decode()
    if not fi_n:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("fi_n es: " + str(fi_n))
    
    #Enviar tem4
    temp4=0
    conn.send(str(temp4).encode())  #envio de paquete a cliente 
    
    #Recivir e
    e = conn.recv(1024).decode()
    if not e:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("e es: " + str(e))
    
    
    #Enviar tem5
    temp5=0
    conn.send(str(temp5).encode())  #envio de paquete a cliente 
    
    #Recivir mensaje cifrado
    mensajecifrado = conn.recv(1024).decode()
    if not mensajecifrado:
            #si no se recive el paquete, se corta la conexion
            conn.close()
    print("el mensaje cifrado es: " + str(mensajecifrado))
    
    
    todo =[]
    todo.append(int(p))
    todo.append(int(q))
    todo.append(int(n))
    todo.append(int(fi_n))
    todo.append(int(e))
    todo.append(mensajecifrado)
    


    conn.close()  #Termino de conexion
    return todo

todo = server()
p = todo[0]
print(p)
q = todo[1]
print(q)
n = todo[2]
print(n)
fi_n = todo[3]
print(fi_n)
e = todo[4]
d = calcula_d(e, fi_n)
mensajecifrado = todo[5]
print(mensajecifrado)
llaveprivada = [n,d]
mensajedescifrado = descifrar_mensaje(mensajecifrado, llaveprivada)

print(mensajedescifrado)
Mensaje_descifrado = open('mensajedescifrado.txt','w+')
Mensaje_descifrado.write(mensajedescifrado)
Mensaje_descifrado.close()

