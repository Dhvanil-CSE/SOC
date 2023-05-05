# echo-server.py

import socket

import json


def pfactor(num):
    l=[]
    while num >1:
        for i in range(2,num+1):
            if(num%i==0):
                l.append(i)
                num=int(num/i)
                break
    return l


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
                    break
                if qval != 'exit':
                    pf_list=pfactor(qval)
                data["result"]=pf_list
                data.pop("data")
                data=json.dumps(data)
                data=data.encode()
                conn.sendall(data)
                
