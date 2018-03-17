#!/usr/bin/python
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("",80))

while True:
   data,client=server.recvfrom(1024)
   print('message from:',client)
   print('message data:',data)
   buf=raw_input("input data:")
   server.sendto(str(buf),client)
server.close()
