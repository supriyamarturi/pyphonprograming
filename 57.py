a,b=map(int,raw_input().split())
list=[int(t) for t in raw_input().split()]
if b in list:
    count=list.count(b)
    print count
else:
    print 0
