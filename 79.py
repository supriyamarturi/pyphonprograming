u,v=map(int,raw_input().split())
c=u*v
for i in range(c+1):
	if (i*i)==c:
		print "yes"
		break
else:
	print "no"
