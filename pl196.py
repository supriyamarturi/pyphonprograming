import sys
z=int(raw_input())
W=[int(y) for y in raw_input().split()]
dic1={}
for y in W :
    dic1[y]=dic1.get(y,0)+1
min1=sys.maxsize
for k,e in dic1.items():
    if e<min1:
        min=e
        key=k
print key
