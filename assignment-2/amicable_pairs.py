from sage.all import *

c=0
a=2
b1=1
while c<10:
	if a!=b1:
		b=int(sum(divisors(a)))-a
		if b!=a and a==int(sum(divisors(b)))-b:
			print("[",a,",",b,"]")
			c=c+1
			b1=b
	a=a+1
