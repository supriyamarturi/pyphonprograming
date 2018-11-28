k = raw_input().rstrip()
digits = []
for l in k:
	if l.isdigit():
		digits.append(l)

print("".join(digits))
