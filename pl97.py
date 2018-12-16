import sys,string, math,itertools
n,k = raw_input().split()
n,k = int(n),int(k)
sum1 = 0
for i in range(n,k+1) :
    if i%2==1 :
        sum1 += i
print(sum1)


