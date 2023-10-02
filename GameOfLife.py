import sys
l=[-34,-33,-32,-1,1,32,33,34]
for i in sys.argv[1:]:
	for j in range(len(i)):
		if (i[j]=='\n'):print()
		else:
			a=0
			if i[j]=='.':
				for k in l:
					try:
						if i[j+k]=='#':a=a+1
					except:a
				print('#',end="")if (a==3)else print('.',end="")
			else:
				for k in l:
					try:
						if i[j+k]=='#':a=a+1
					except:a
				print('#',end="")if (a==2 or a==3)else print('.',end="")
