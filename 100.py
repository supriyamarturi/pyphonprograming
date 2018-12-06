num=int(raw_input())
def calcProduct(k):
	if(len(str(k)) == 1):
		return k
	else:
		return (k%10 * calcProduct(k/10))
print(calcProduct(2143))
