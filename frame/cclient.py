#!/usr/bin/env python3

import socket, sys, re, time, os
sys.path.append("../lib")       # for params
import params

host = "127.0.0.1"  # every machines has thid address
port = 50001     # port number reserved
SIZE_B = 1024   # buffer size to be read

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s is a factory for connected sockets

s.connect((host,port))

with open ("file", "wb") as fl:

    print("File opened successfully")

    while True:

        print("Getting data...")
        data = s.recv(SIZE_B)    # we assign received data to object data
        print("data: ",  (data))


        if not data:           # stop if there is no data


            break


        break

fl.close()
print("File received successfully!") # signalling of file received
s.close()                            # close socket

print("The connection has been closed") # signalling of closed connection
