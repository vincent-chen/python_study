import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
  buff=input("send something to server:")
  client.sendto(str(buff),('127.0.0.1',80))
  data,server=client.recvfrom(1024)
  print("message from server:", data)
  print("server:", server)
client.close()

