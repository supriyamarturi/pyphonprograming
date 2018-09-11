def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1)+fib(n-2))
n=int(raw_input())
for i in range(1,n+1):
    print fib(i),

