#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

UDP_IP_ADDRESS = "localhost"
UDP_PORT_NO = 1234

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = str(input("Enter your message: "))
    msg = msg.encode()
    clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))

