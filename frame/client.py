#! /usr/bin/env python3

import socket, sys, re, time, os
sys.path.append("../lib")       # for params
import params

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s is a factory for connected sockets

host = "127.0.0.1"   # every machine has this address
port = 50001   # port number reserved
SIZE_B = 1024   # buffer size to be read

s.connect((host, port))
s.send("Hello, there!".encode()) # greeting message to server

with open ("file", "wb") as fl:
    print("File opened successfull")

    while True:
        print("Getting data...")
        data = s.recv(SIZE_B)    # we assign received data to object data
        print("data: %s", (data))

        if not data:           # stop if there is no data
            break

        break

fl.close()

s.shutdown(socket.SHUT_WR)

print("Zero length read.  Closing") 
s.close()

'''''
Notes:

with open() python 3 function opens a file, and returns it as a file object. "w" stands for openning a file for writing, or creates a file if it is non-existent. "b" stands for handling the file in binary.

'''''
