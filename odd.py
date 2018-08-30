lower,upper = map(int,raw_input().split())
for i in range(lower,upper+1):
    if(i%2!=0) and i!=1:
        print i,
