from sage.all import *
import random
class rsa_class:
    def __init__(self,k,e=65537):
        p1=random_prime(2**k,True,2**(k-1))
            
        p2=random_prime(2**k,True,2**(k-1))
            
        self.N=p1*p2
        self.e=e
        if gcd(self.e,euler_phi(self.N))!=1:
            while True:
                self.e=random.randint(1,2**k)
                if gcd(self.e,euler_phi(self.N))==1 and self.e!=1:
                    break
        print(e)    

    def get_public_key(self):
        self.pk=(self.e,self.N)
    def encrypt(self,plaintext):
        if plaintext>=self.pk[1]:
            return "error"
        M=mod(plaintext**int(self.pk[0]),int(self.pk[1]))
        return M
    def decrypt(self,cipher):
            d=inverse_mod(self.pk[0],euler_phi(self.pk[1]))
            m=mod(cipher**d,self.pk[1])
            return m
        
        

k=int(input())
o=rsa_class(k)
o.get_public_key()
m=int(input("Enter your secret message : "))
cipher=o.encrypt(m)
if cipher!="error":
    ptext=o.decrypt(cipher)
    if ptext!="error":
        print("cipher is",cipher)
        print("plain text is",ptext)
    else:
        print("error")
else:
    print("error")