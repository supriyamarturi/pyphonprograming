a = raw_input().rstrip()
aLen = len(a)
mid = aLen >> 1
if (aLen & 1):
	print(a[:mid] + "*" + a[mid+1:])
else:
	print(a[:mid-1] + "**" + a[mid+1:])
