a,b = map(int,raw_input().split())
a = a ^ b
b = a ^ b
a = a ^ b
print("  {0} {1}" .format (a,b))
