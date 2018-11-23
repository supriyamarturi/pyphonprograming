d,e=map(int,raw_input().split())
x=d*e
for i in range(x+1):
	if (i*i)==x:
		print "yes"
		break
else:
	print "no"
