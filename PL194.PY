s,d=map(str,raw_input().split())
if s=='P' and d=='R' or s=='R' and d=='P':
    print('P')
elif s=='P' and d=='S' or s=='S' and d=='P':
    print('S')
elif s=='S' and d=='R' or s=='R' and d=='S':
    print('R')
elif s=='S' and d =='S':
    print('D')
elif s=='P' and d=='P':
    print('D')
elif s=='R' and d=='R':
    print('D')
