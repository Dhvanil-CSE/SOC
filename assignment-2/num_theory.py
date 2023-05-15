from sage.all import *
import random
k=int(input())
plist=[]
for i in range(10**(k-1),10**k):
	c=1
	for j in range(2,i//2+1):
		if i%j==0:
			c=0
			break
	if c==1:
		plist.append(i)
p1=random.choice(plist)
plist.remove(p1)
p2=random.choice(plist)

a=inverse_mod(p1,p2)
b=inverse_mod(p2,p1)-p1

print("(",p1,",",p2,",",a,",",b,")")

