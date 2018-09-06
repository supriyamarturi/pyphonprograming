lower,upper=map(int,raw_input().split())
for n in range(lower+1,upper):
    if(n>1):
        for i in range(2,n):
            if(n % i)==0:
                break
        else:
            print(n)
