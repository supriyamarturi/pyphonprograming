import sys,string, math,itertools
s = int(raw_input())
D = [ int(h) for h in raw_input().split()]
ans = D[0]
for i in range(1,s) :
    ans = ans ^ D[i]
print(ans)





