from sage.all import *
import random
k=int(input())
p1=random_prime(10**k-1,10**k)
p2=random_prime(10**k-1,10**k)

a=inverse_mod(p1,p2)
b=inverse_mod(p2,p1)-p1

print("(",p1,",",p2,",",a,",",b,")")

