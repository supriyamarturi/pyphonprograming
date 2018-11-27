s=int(raw_input())
list=[int(c) for c in raw_input().split()]
list.sort()
print " ".join(map(str,list))
