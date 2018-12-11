t,d=map(int,(raw_input()).split())
if(t>d):
    p=t
else:
    p=d
while(True):
    if((p%t==0) and (p%d==0)):
        l=p
        break
    p+=1
print(l) 



