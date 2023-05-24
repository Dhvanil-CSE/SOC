from sage.all import *
import random
class elgamal_class:
    def __init__(self,p,g):
        self.B=1
        self.p=p #586069695452241770718895237154794403533331590789
        self.g=g #567
        while self.B==1:
            self.b=random.randint(1,100)
            self.B=mod(self.g**self.b,self.p)
            if self.B!=1:
                break
    def get_public_key(self):
        self.pubk=(self.p,self.g,self.B)
        return self.pubk
    def encrypt(self,pubk,m):
        m=m.encode()
        m=m.hex()
        m=int(m,16)
        if m<self.p:
            a=random.randint(1,100)
            s=mod(pubk[2]**a,pubk[0])
            A=mod(pubk[1]**a,pubk[0])
            X=mod(m*s,pubk[0])
            Asend=(A,X)
            return Asend
        else:
            return "error"
    def decrypt(self,cipher):
        if cipher=="error":
            return "error m>=n"
        self.Asend=cipher
        s=mod(self.Asend[0]**self.b,self.p)
        invs=inverse_mod(s,int(self.p))
        M=mod(self.Asend[1]*invs,self.p)
        M=hex(M)
        M=M[2:]
        M=bytearray.fromhex(M).decode()
        return M
    
'''p=int(input("enter p: "))
g=int(input("enter G: "))
m=input()
o=elgamal_class(p,g)
pubk=o.get_public_key()

cipher=o.encrypt(pubk,m)
ptext=o.decrypt(cipher)

print(ptext)'''
