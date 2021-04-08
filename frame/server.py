#! /usr/bin/env python3

import socket, sys, re, os
sys.path.append("../lib")       # for params
import params

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s is a factory for connected sockets

ip = "127.0.0.1"  # every machines has this address
port = 50001   # port number reserved
s.bind((ip,port))
s.listen(1)              # allow only one outstanding request

while True:
    conn, addr = s.accept() # wait until incoming connection request (and accept it)
    print("Connected by ", addr)
    data = conn.recv(SIZE_B).decode() #amount of bytes decoded

    print("Server", repr(data))
    
    nameFile = "file.txt"
    op = open(nameFile, "rb")
    re = op.read(SIZE_B)

    while(1):
        conn.send(1)
        print("Sent content ", repr(1))
        re = op.read(SIZE_B)
        break

    op.close()
    break



conn.shutdown(socket.SHUT_WR)
conn.close()
s.close()
'''''
The repr() python 3 function takes a single parameter and returns
a printable representation of the object.

The open() python 3 function opens a file, and returns it as a file object. "r" stands for opening and reading a file. If the file is non-existent, it gives you an error. "b" stands for handling the file in binary.

'''''
