from sage.all import *
import random
k=int(input())
plist=prime_range(10**k-1,10**k)
p1=random.choice(plist)
plist.remove(p1)
p2=random.choice(plist)

a=inverse_mod(p1,p2)
b=inverse_mod(p2,p1)-p1

print("(",p1,",",p2,",",a,",",b,")")

