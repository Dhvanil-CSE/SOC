# echo-server.py
from sage.all import *
import socket

import json

def pfactor(n):
	n_factor=list(factor(n))
	n_factor_list=[]
	for i in range(len(n_factor)):
		for j in range(n_factor[i][1]):
			n_factor_list.append(int(n_factor[i][0]))
	print(n_factor_list)

	return n_factor_list


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65412  # Port to listen on (non-privileged ports are > 1023)
a=0
while a==0:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(10024)
                if not data:
                    break
                data=data.decode("utf-8")
                data=json.loads(data)
                qval=data["data"]
                if qval=='exit':
                    a=1
                    pf_list=qval
                if qval != 'exit':
                    pf_list=pfactor(qval)
                data["result"]=pf_list
                data.pop("data")
                data=json.dumps(data)
                data=data.encode()
                conn.sendall(data)

                
