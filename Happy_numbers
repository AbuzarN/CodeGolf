def r(a,b):
	t=0
	for i in a:t+=int(i)**2
	if t==1:return True
	elif t in b:return False
	else:b.append(t);return True if r(str(t),b)else False
for i in range(1,200):
	if r(str(i),[]):print(i)
