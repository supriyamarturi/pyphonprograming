s=int(raw_input())
a=[]
while(s>0):
    dig=s%10
    a.append(dig)
    s=s//10
print sum(a)
