import sys,string, math,itertools
f,g = raw_input().split()
g = int(g)
for i in range(0,g+1) :
    h = str(i)
    if h not in f :
        print('no')
        sys.exit()
print('yes')
