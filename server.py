#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading
import time
threads = []
inputs = []
thread_id = 0
total_threads = 4

UDP_IP_ADDRESS = "localhost"
UDP_PORT_NO = 1234

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


def input_thread():
    turn = 0
    while True:
        data, addr = serverSock.recvfrom(1024)
        str = data.decode()
        inputs[turn].append(str)
        turn = (turn+1) % total_threads


def operation(id):
    while True:
        if len(inputs[id]) == 0:
            continue
        print(threading.current_thread().name,":",inputs[id].pop())
        time.sleep(1)
    
t = threading.Thread(target = input_thread)
t.start()
    
for i in range(total_threads+1):
    thread = threading.Thread(target = operation, args = (thread_id,))
    threads.append(thread)
    inputs.append([])
    thread_id += 1
        
for t in threads:
    t.start()
    time.sleep(1)
    
for t in threads:
    t.join()
        

