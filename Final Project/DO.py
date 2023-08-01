import random

import gmpy2
from decimal import Decimal
from sage.all import *
import pickle
import socket
import pandas as pd
import numpy as np
from numpy import random

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

#pi_inverse func
def pi_inverse(j,pi):
    for i in range(len(pi)):
        if(pi[i]==j):
            return i
            
#paillier class
def p_encrypt(n,g,m):
    r=random.randint(1,n-1)
    cipher1=pow(int(g),int(m),int(n)**2)
    cipher2=pow(int(r),int(n),int(n)**2)
    cipher=cipher1*cipher2
    return cipher

#paillier encrypted query to Aq
def A_form(pi,M,q_encrypted,pubk,d,c,epsilon):
    eta=d+c+epsilon+1
    beta_q=Decimal(random.randint(10))
    R_q=random.randint(10,size=c)
    A_q=np.zeros(eta)
    for i in range(eta):
        A_q[i]=Decimal(p_encrypt(pubk[0],pubk[1],0))
        for j in range(eta):
            t=(pi_inverse(j,pi))
            if(t<d):
                phi=int(beta_q*int(M[i,j]))
                # if(phi>0):
                print("q",type(q_encrypted[t]))
                print(type(A_q[i]))
                print(phi)
                A_q[i]=str(gmpy2.mpz(gmpy2.mpz(float(A_q[i]))*pow(gmpy2.mpz(float(q_encrypted[t])),gmpy2.mpz(float(phi)),gmpy2.mpz(int(pubk[0]**2)))))
                print("a",A_q[i])
                # else:
                #     A_q[i]=A_q[i]/(int(q_encrypted[t])**abs(int(phi)))

            elif(t==d):
                phi=int(beta_q*int(M[i,j]))
                A_q[i]=(A_q[i]*p_encrypt(int(pubk[0]),int(pubk[1]),phi))
                print("a",A_q[i])
            elif(t<=d+c):
                omega=t-d-1
                phi=(beta_q*int(M[i,j])*int(R_q[omega]))
                print(phi)
                A_q[i]=(A_q[i]*int(p_encrypt(int(pubk[0]),int(pubk[1]),phi)))
                print("a",A_q[i])
    return A_q





#function for computing Ddot
def perturb_pi(a,b,c,d1,ax,n,pi):
    
    
    D_prime=np.concatenate((a,b,c,d1),axis=ax)
    
    D_prime=np.transpose(D_prime)
    D_prime2 = np.array(D_prime)
    for i in range(n):
        D_prime[pi[i]]=D_prime2[i]
    D_prime=np.transpose(D_prime)
    
    return D_prime

#DO approval
def DOapproval(DOreturn,q_encrypted,pubk):
#if approved
#A_i computation
    if(DOreturn==1):
        tvar=1
        print(type(pi))
        print(type(M))
        print(type(q_encrypted))
        print(type(pubk))
        print(type(d))
        print(type(c))
        print(type(epsilon))
        A=A_form(pi,M,q_encrypted,pubk,d,c,epsilon)
        return A,tvar
#if not
    elif(DOreturn==0):
        tvar=0
        return q_encrypted,tvar

#dimension d and number n
d=50

n=10000

#security parameters
c=random.randint(1,10)
epsilon=random.randint(1,10)

#invertible matrix M 
while True:
    M=np.random.randint(low=0,high=5, size=(d+c+epsilon+1,d+c+epsilon+1))
    if np.linalg.det(M) !=0:
         break
#(d+1) dimension vector S
S=random.randint(8,size=d+1)

# c-dimensional tou
tou=random.randint(8,size=c)

#doubtful
# tou=np.multiply(np.ones((n,c)),tou)

#permutation pi
pi=np.arange(d+c+1+epsilon)
random.shuffle(pi)

DO_key=[S,tou,pi,M]

#DBencryption
#datapoints
D=pd.read_csv("database.txt",header=None)
D=D.to_numpy()
print(D.shape)
# D=np.random.randint(low=-10,high=11, size=(n,d))

#computing the reuirements of pidot(Ddot)
V=random.randint(11,size=(n,epsilon))
pmag=(np.sum(np.square(D),axis=1)).reshape(n,1)
D_prime_1=S[0:d]-2*D
D_prime_2=S[d]+pmag
tou=np.multiply(np.ones((n,c)),tou)

#computing Ddot
D_dot=np.matmul(perturb_pi(D_prime_1,D_prime_2,tou,V,1,d+c+1+epsilon,pi),np.linalg.inv(M))
#upload the above D_dot to CS
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9998  # Port used for connection of CS an DO
# a=0
# while a==0:
print(D_dot)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # D_dot_send={"D_dot":D_dot.tolist()}
    # D_dot_send=json.dumps(D_dot_send)
    # D_dot_send=D_dot_send.encode()
    #s.sendall(D_dot_send)
    send_array(s,D_dot)
    # resp1=s.recv(10024) #data sent
    # print(resp1.decode())
    s.close()
#after DO receives the pubk and ciph from QU
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT2 = 65412  # Port used for connection of QU an DO
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT2))
    s.listen()
    conn, addr = s.accept()

    with conn:
                    data=receive_array(conn)
                    pubk=data[0:2]
                    q_received=data[2:]
                    print(pubk)
                    
                    print(q_received)
                    
                    approve=int(input("DO YOU WANT TO APPROVE THE QUERY ( 1 for yes 0 for no ) :"))
                    A_q, mvar =DOapproval(approve,q_received,pubk)
                    print(A_q)
                # print(f"Connected by {addr}")
                # while True:
                #     data = conn.recv(10024)
                #     if not data:
                #         resp2="not received"
                #         conn.send(resp2.encode())
                #         break
                #     # resp2="query received"
                #     # conn.send(resp2.encode())
                #     data=data.decode("utf-8")
                #     data=json.loads(data)
                #     pubk=data["pubk"]
                #     q_received=data["cipher"]
#send the A_q to QU
                    # if(A_q==0):
                    #     A_qsend={"A_q":"Not allowed"}
                    # else:
                    
                    A=pickle.dumps({"A_q":A_q,"var":mvar})
                    conn.sendall(A)
                    print("hello")
                    # resp3=conn.recv(10024)
                    # print(resp3.decode())
