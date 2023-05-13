from sage.all import *
n=int(input())
c=1
for carmi in range(2,n+1):
	c=1
	f=list(factor(carmi))
	for i in f:
		if i[1]>=2:
			c=0
	if sigma(carmi,0)>2:

		plist=prime_divisors(carmi)
		for i in plist:
			if (int(carmi)-1)%(int(i)-1)!=0:
				c=0
				break
		if c==1:
			print(carmi)
