# echo-client.py

import socket
import json

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
a=0
while a==0:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        x=input()
        if x!='exit':
            x=int(x)
        if x=='exit':
            a=1
        json_dic={"query":x}
        json_dic=json.dumps(json_dic)
        json_dic=json_dic.encode()
        s.sendall(json_dic)
        data1 = s.recv(10024)

        

    PORTI = 65412
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORTI))
        s.sendall(data1)
        fdata = s.recv(10024)
        fdata=fdata.decode("utf-8")
        fdata=json.loads(fdata)
        qval=fdata["result"]
        print(qval)