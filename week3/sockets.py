# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org',80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\n'.encode()
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())

mySocket.close()