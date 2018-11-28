C,D=map(int,raw_input().split())
if(C>D):
    min2=C
else:
    min2=D
while(1):
    if(min2%C==0 and min2%D==0):
        print(min2)
        break
    min2=min2+1
