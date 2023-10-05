import sys;p=print;q=int
def a (n,d):
	if n==0 or d==1:p(str(n)+"/1")
	else:
		for i in reversed(range(1,max(n,d)+1)):
			if n%i==0 and d%i==0:p(str(q(n/i))+"/"+str(q(d/i)));break
for i in sys.argv[1:]:b=i.split('/');a(q(b[0]),q(b[1]))
