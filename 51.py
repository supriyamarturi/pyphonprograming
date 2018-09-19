n=int(raw_input())
a=[]
while(n>0):
    dig=n%10
    a.append(dig)
    n=n//10
print a [::-1] 
