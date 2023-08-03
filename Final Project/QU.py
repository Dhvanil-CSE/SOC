from sage.all import *
import random
import numpy as np
import socket
import json
from decimal import *
import pickle

def receive_array(client_socket):
    data = b""
    while True:
        packet = client_socket.recv(1024000000)
        if not packet:
            break
        data += packet
        if len(packet) < 4096:
            break
    return pickle.loads(data)

def send_array(client_socket, data):
    serialized_data = pickle.dumps(data)
    client_socket.sendall(serialized_data)

class paillier_class:
    
    def __init__(self):
        c=1
        while c==1:
            p1=random_prime(2**5,True,2**4)            
            p2=random_prime(2**5,True,2**4)
            if p1!=p2 and gcd(p1*p2,(p1-1)*(p2-1)==1):
                break
        #self.func = lambda x : (x-1)//n
        n=int(p1*p2)
        self.n=n
        self.lam=int(lcm(p1-1,p2-1))
        #a=(mod(g**self.lam,n**2))
        a=0
        self.a=a
        while True :
            g=int(random.randint(1,n**2-1))
            self.g=g
            L=pow(g,self.lam,n**2)
            self.a=(int(L)-1)//self.n
            if gcd(self.a,n)==1 and gcd(self.g,n)==1 :
                break
        self.u=int(inverse_mod(self.a,n))
    
    def get_public_key(self):
        self.pubk=(self.n,self.g)
        return self.pubk
    
    #Encryption func
    def encrypt(self,m):
        
            r=random.randint(1,self.n-1)
            cipher1=pow(self.g,m,self.n**2)
            cipher2=pow(r,self.n,self.n**2)
            cipher=cipher1*cipher2
            
            return cipher
    #Decryption func
    def decrypt(self,cipher):
        
        t=pow(cipher,self.lam,self.n**2)
        k=(int(t)-1)//int(self.n)
        m=mod(k*self.u,self.n)
        
        return m

d=50
o=paillier_class()
pubk=o.get_public_key() #(I)QU generates a public key pair {pk, sk} of homomorphic cryptosystem
# print(pubk[0])
sg = input("Enter your query string with space as value separator : ")
ar = sg.split(" ")
q=[]
for i in ar:
    q.append(int(i))
#q is the query
# q=np.random.randint(low=-10,high=11,size=(d))
# print(q)
ciph=np.random.randint(low=-10,high=11,size=(d))
for i in range(d):
    m=int(q[i])
    cipher=o.encrypt(m)
    ciph[i]=cipher

#ciph is the paillier encrypted query i.e. {Epk(q1), Epk(q2), . . . , Epk(qd)}

# Send the pubk and ciph to DO
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT2 = 65412  # Port used for connection of QU an DO
a=0
# while a==0:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT2))
        pubkciph=np.concatenate((pubk,ciph))
        send_array(s,pubkciph)
        # print("send")
        # json_dic={"pubk":pubk,"cipher":ciph.tolist()}
        # json_dic=json.dumps(json_dic)
        # json_dic=json_dic.encode()
        # s.sendall(json_dic)
        # resp2 = s.recv(10024) #Query to DO sent
        # print(resp2.decode())
#Receives A_q from DO
        print("Waiting for query to be approved...")
        A_q=pickle.loads(s.recv(1024000000))
        mvar=A_q["var"]
        A_q=A_q['A_q']
        
        s.close()
if(mvar==0):
    print("query denied")
else:
#pt is just an array for pailler decrypted query
    pt=np.random.randint(low=-10,high=11,size=(len(A_q)))
    for i in range(len(A_q)):
        m=int(A_q[i])
        ptext=o.decrypt(m)
        if(ptext>1000):
            ptext=int(ptext)
            ptext-=pubk[0]
            
        pt[i]=ptext
    # print(pt)
    print("Query uploaded to CS....")
    #upload pt to CS

HOST2 = "127.0.0.1"  # The server's hostname or IP address
PORT3 = 9998  # Port used for connection of QU an CS
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST2, PORT3))
    if(mvar!=0):
        nvar=1
        A=pickle.dumps({"pt":pt,"var":nvar})
        s.sendall(A)
        lst=pickle.loads(s.recv(1024000000))
        lst=lst["A_q"]
        print("k-NN datapoints found : ",lst)
    else:
        nvar=0
        A=pickle.dumps({"pt":"Not Allowed","var":nvar})
        s.sendall(A)
        # pt_send={"pt":pt}
        # pt_send=json.dumps(pt_send)
        # pt_send=pt_send.encode()
        # s.sendall(pt_send)
        # resp3=s.recv(10024)
        # print(resp3.decode())
