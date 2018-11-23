s = raw_input().rstrip()
sLen = len(s)
mid = sLen >> 1
if (sLen & 1):
	print(s[:mid] + "*" + s[mid+1:])
else:
	print(s[:mid-1] + "**" + s[mid+1:])
