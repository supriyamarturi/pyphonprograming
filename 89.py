def sort(values):
	for i in range(len(values)):		
		for j in range(i, len(values)):			
			if (values[i] > values[j]):
				temp = values[i]
				values[i] = values[j]
				values[j] = temp
 s = raw_input().rstrip()
sList = list(s)
sortsList)
print("".join(sList))
