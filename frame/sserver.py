#! /usr/bin/env python3

import socket, sys, re, time, os
sys.path.append("../lib")       # for params
import params
from threading import Thread

host = "127.0.0.1"   # every machine has this address
port = 50001   # port number reserved
SIZE_B = 1024   # buffer size to be read

class Threads(Thread):

    def __init__(self, ip, port, socket):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("Opening thread for "+ip+":"+str(port))

    def r(self):
        nameFile = "file.txt"
        op = open(nameFile, "rb")
        while True:
            length = op.read(SIZE_B)

            while (lenght):
                self.socket.send(length)
                length = op.read(SIZE_B)

            if not length:
                op.close()
                self.socket.close()
                break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
thread = []

while True:
    s.listen(2)
    print("Awaiting connections...")
    conn, (ip,port) = s.accept()

    print("Connected by ", (host,port))
    nthread = Threads(host,port,conn)
    nthread.start()
    thread.append(nthread)

for th in thread:
    th.join()

conn.shutdown(socket.SHUT_WR)
conn.close()
