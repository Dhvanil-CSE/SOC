import random
# echo-server.py

import socket
import json

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
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
                qval=data["query"]
                if qval!='exit':
                    x=random.randint(1,10000)
                    print(x)
                    qval=qval*x
                data["data"]=qval
                data.pop("query")
                data=json.dumps(data)
                data=data.encode()
                conn.sendall(data)
                if qval=='exit':
                    a=1