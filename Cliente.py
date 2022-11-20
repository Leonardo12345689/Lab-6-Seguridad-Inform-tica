#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:35:10 2022

@author: carlofaundez
"""


import socket







#Funcion para verificar si el numero es primo
def verifica_primo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False
    


def pq():
	
	p=int(input("Ingrese Valor de primer número primo (p)\n:"))
	while verifica_primo(p)==False:
		print("\p tiene que ser primo")
		p=int(input("\nIngrese Valor de primer número primo (p)\n:"))
	q=int(input("Ingrese Valor de segundo número primo (q)\n:"))
	while verifica_primo(q)==False or q==p:
		print("q tiene que ser primo o distinto de p")
		q=int(input("\nIngrese Valor de segundo número primo (q)\n:"))
	listapq=[p,q]
	return listapq

    
    
#Funcion para generar lista de primos para e
def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if verifica_primo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp



#Funciones para hacer calculo de e obteniendo maximo comun divisor
def calcula_e(fi_n):
	e=2
	lista_e=[]
	while e>1 and e<fi_n :
		if mcd(e,fi_n)==1:
			lista_e.append(e)
			e=e+1
		else:
			e=e+1
	print("\nPosibles valores para e:\n"+str(lista_e))
	e=int(input("\nIngrese valor de e que se encuentre en la lista\n:"))
	while mcd(e,fi_n)!=1:
		print("\nSeleccione un valor valido que este en la lista")
		e=int(input("\nIngrese valor de e que se encuentre en la lista\n:"))
	return e


def mcd(e,fi_n):
	m=fi_n%e
	while m!=0:
		fi_n=e
		e=m
		m=fi_n%e
	return e





###############################Cifrado############################################

#Funcion para cifrar mensaje
def cifrar_mensaje(msj,key):
	msj=msj.upper()
	lm=msj.split(" ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=cifrar_palabra(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc


#Funcion para cifrar palabra, esta funcion es usada por la que cifra el mensaje
def cifrar_palabra(m,k):
	lpc=[]
	lp=[]
	n,e=k
	cpc=""
	for i in m:
		x=buscarpos(i)
		lp.append(x)
	for j in lp:
		c=(j**e)%n
		lpc.append(c)
	for k in lpc:
		cpc=cpc+str(k)+" "
	return cpc

#Funcion para encontrar la posicion numerica de una letra en el abecedario, entregando el numero
def buscarpos(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1	








def client(p,q,n,fi_n,e,mensajecifrado):
    host = "127.0.0.1"
    port = 1234

    client_socket = socket.socket()  # Inicio
    client_socket.connect((host, port))  # Conectar al servidor

    #enviar P
    client_socket.send(str(p).encode())

    #Recivir temp
    temp = int(client_socket.recv(1024).decode())

    #enviar q
    client_socket.send(str(q).encode())

    #Recivir temp2
    temp2 = client_socket.recv(1024).decode()


    #enviar n
    client_socket.send(str(n).encode())
    
    #Recivir temp3
    temp3 = client_socket.recv(1024).decode()


    #enviar fi de n
    client_socket.send(str(fi_n).encode())

    #Recivir temp4
    temp4 = client_socket.recv(1024).decode()
    
    #enviar e
    client_socket.send(str(e).encode())
    
    #Recivir temp5
    temp5 = client_socket.recv(1024).decode()
    
    #enviar mensaje cifrado
    client_socket.send(str(mensajecifrado).encode())
    
    



    client_socket.close()  # close the connection


pq = pq()
p = pq[0]
q = pq[1]
n = p * q
fi_n = (p-1)*(q-1)
e = calcula_e(fi_n)

llavepublica = [n,e]
archivo_entrada = open('mensajeentrada.txt', 'r')
mensaje = archivo_entrada.readlines()
mensaje = str(mensaje[0])
print(mensaje)
mensajecifrado= cifrar_mensaje(mensaje,llavepublica)
mensajecifrado = mensajecifrado[0:len(mensajecifrado)-2]
print(mensajecifrado)


if __name__ == '__main__':
    client(p,q,n,fi_n,e,mensajecifrado)
