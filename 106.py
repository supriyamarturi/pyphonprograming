
def findK(n, k): 
    half = int((n + 1) / 2) 
    if k > n: 
        return (2 * (k - half)) 
    else: 
        return (2 * k - 1) 
          
# Driver code 
n = 10
k = 3
print(findK(n, k)) 
