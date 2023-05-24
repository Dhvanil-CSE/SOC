from sage.all import *
import random
class rsa_class:
    def __init__(self,k,e=65537):

        while True:
            p1=random_prime(2**k,True,2**(k-1))
            
            self.euler_p1=p1-1
            p2=random_prime(2**k,True,2**(k-1))
            self.euler_p2=p2-1
            self.p1=p1
            self.p2=p2
            if p1!=p2:
                break
        self.N=self.p1*self.p2
        self.e=e
        if gcd(self.e,self.euler_p1*self.euler_p2)!=1:
            while True:
                self.e=random.randint(1,2**k)
                if gcd(self.e,self.euler_p1*self.euler_p2)==1 and self.e!=1:
                    break 

    def get_public_key(self):
        self.pk=(self.e,self.N)
    def encrypt(self,plaintext):
        plaintext=plaintext.encode()
        plaintext=plaintext.hex()
        
        plaintext=int(plaintext,16)

        if plaintext>=self.pk[1]:
            return "error"
        M=mod(plaintext**int(self.pk[0]),int(self.pk[1]))
        return M
    def decrypt(self,cipher):
            if cipher!="error":

                d=inverse_mod(self.pk[0],(self.euler_p1*self.euler_p2))
                m=mod(cipher**d,self.pk[1])
                m=hex(m)
                m=m[2:]
                m=bytearray.fromhex(m).decode()
                return m
            else:
                print("error -1")

'''k=int(input())
o=rsa_class(k)
o.get_public_key()
m=input("Enter your secret message : ")
cipher=o.encrypt(m)
ptext=o.decrypt(cipher)
print(ptext)'''
