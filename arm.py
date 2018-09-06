lower,upper=map(int,raw_input().split())
for m in range(lower+1,upper):
    if(m>1):
        for i in range(2,m):
            if(m % i)==0:
                break
        else:
            print(m)


