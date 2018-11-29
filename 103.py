x= raw_input().rstrip()
newWordBegins = True
result = ''
for z in x:
	if z == ' ':
		newWordBegins = True		
	elif newWordBegins:
		newWordBegins = False
		z = chr(ord(z) - 32)
	result += z

print(result)
