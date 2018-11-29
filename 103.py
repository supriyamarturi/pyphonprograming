k= raw_input().rstrip()
newWordBegins = True
result = ''
for y in k:
	if y == ' ':
		newWordBegins = True		
	elif newWordBegins:
		newWordBegins = False
		y = chr(ord(y) - 32)
	result += y

print(result)
