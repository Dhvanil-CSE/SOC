from sage.all import *
import random
class paillier_class:
    
    def __init__(self,k):
        c=1
        while c==1:
            p1=random_prime(2**k,True,2**(k-1))            
            p2=random_prime(2**k,True,2**(k-1))
            if p1!=p2 :
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
            if gcd(self.a,n)==1 :
                break
        self.u=int(inverse_mod(self.a,n))
    
    def get_public_key(self):
        self.pubk=(self.n,self.g)
        return self.pubk
    def encrypt(self,m):
        m=m.hex()
        m=int(m,16)
        if m<self.n:
            r=random.randint(1,self.n-1)
            cipher1=pow(self.g,m,self.n**2)
            cipher2=pow(r,self.n,self.n**2)
            cipher=cipher1*cipher2
            
            return cipher
        else:
            return "error"
    def decrypt(self,cipher):
        if cipher=="error":
            return "error message>=n"
        t=pow(cipher,self.lam,self.n**2)
        k=(int(t)-1)//int(self.n)
        m=mod(k*self.u,self.n)
        m=hex(m)
        m=m[2:]
        m=bytearray.fromhex(m)
        return m

k=int(input())
o=paillier_class(k)
pubk=o.get_public_key()
m=input("enter message : ")
cipher=o.encrypt(m)
ptext=o.decrypt(cipher)

print(ptext)
