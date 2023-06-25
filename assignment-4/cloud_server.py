# echo-server.py

import socket

import json
def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            factors.append((divisor, count))
        divisor += 1
    return factors

def pfactor(n):
	n_factor=prime_factors(n)
	n_factor_list=[]
	for i in range(len(n_factor)):
		for j in range(n_factor[i][1]):
			n_factor_list.append(int(n_factor[i][0]))
	print(n_factor_list)

	return n_factor_list


HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 3000 # Port to listen on (non-privileged ports are > 1023)
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
                qv=str(qval)
                qd = open("qdata/qdata.txt", "a")
                qd.write(qv)
                qd.write("\n")
                qd.flush()
                if qval=='exit':
                    a=1
                    pf_list=qval
                if qval != 'exit':
                    pf_list=pfactor(qval)
                data["result"]=pf_list
                pl=str(pf_list)
                data.pop("data")
                data=json.dumps(data)
                fd = open("fdata/fdata.txt", "a")
                fd.write(pl)
                fd.write("\n")
                fd.flush()
                data=data.encode()
                conn.sendall(data)
                

                
