num=int(raw_input())
def calcProduct(n):
	if(len(str(n)) == 1):
		return n
	else:
		return (n%10 * calcProduct(n/10))
print(calcProduct(2143))
