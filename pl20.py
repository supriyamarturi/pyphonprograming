s=raw_input()
l=len(s)
m=list(s)
for i in range(l):
    m[i]=ord(s[i])+3
for j in range(l):
    m[j]=chr(m[j])
print ''.join(m)

    

