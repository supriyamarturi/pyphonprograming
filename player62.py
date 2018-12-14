f=int(raw_input())
for k in range(1,f+1):
  if(f%k==0):
    ch=f/k
  if(ch%2==1):
    ans=k
    break
print(ans)






