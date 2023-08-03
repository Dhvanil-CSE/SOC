import random
#from sage.all import *

import socket
import time
import gzip
import json
import numpy as np
from numpy import random
import pickle
# def receive_array(client_socket):
#     data = b""
#     while True:
#         packet = client_socket.recv(1024000000)
#         if not packet:
#             break
#         data += packet
#         if len(packet) < 4096:
#             break
#     return pickle.loads(data)
def receive_array(client_socket):
    data = b""
    while True:
        packet = client_socket.recv(4096)
        if not packet:
            break
        data += packet

    return pickle.loads(data)
def send_array(client_socket, data):
    serialized_data = pickle.dumps(data)
    client_socket.sendall(serialized_data)

#Function to compare distances
def kNNdist(D,query,k):
    buff=np.matmul(D,np.transpose(query))
    buff=buff.reshape(-1)
    buff2=np.sort(buff)
    ind_arr=np.zeros(k)
    for i in range(k):
        for j in range(n):
            if(buff2[i]==buff[j]):
                ind_arr[i]=j
                break
    return ind_arr


#receives Ddot from DO
HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 9998  # Port used for connection of CS an DO
# a=0
# while a==0:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    print(f"Connected by {addr}")
    with conn:
        #data = conn.recv(10000024)
        D_dot_received = receive_array(conn)
        
        # print(D_dot_received)     
        print("Database updated")     
        s.close()
        conn.close()
            # if not data:
            #     resp1="not received"
            #     conn.send(resp1.encode())
            #     break
            # resp1="D_dot received"
            # conn.send(resp1.encode())
            
            # data=data.decode("utf-8")
            # data=json.loads(data)
            # D_dot_received=data["D_dot"]

#receives pt i.e. q' from QU
n=10000
k=10
HOST2 = "0.0.0.0"  # The server's hostname or IP address
PORT3 = 9998  # Port used for connection of QU an CS
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST2, PORT3))
        s.listen()
        conn, addr = s.accept()
        with conn:
            cr=conn.recv(1024000000)
            # print("QU sent a Query....Showing results...")
            
            result1=pickle.loads(cr)
            q_prime=result1['pt']
            nvar=result1["var"]
            # print(q_prime)
            # print(f"Connected by {addr}")
            # while True:
            #     data = conn.recv(100024)

            #     if not data:
            #         break
            #     pt=data.decode("utf-8")
            #     pt=json.loads(pt)
                # q_prime=pt["pt"]
            if(nvar==1):
    

                index_set=kNNdist(D_dot_received,q_prime,k)
                print("The K- nearest datapoint indexes sent")
                A=pickle.dumps({"A_q":index_set,"var":nvar})
                conn.sendall(A)