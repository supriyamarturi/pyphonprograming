year=int(raw_input())
if(year%4==0):
    print("yes")
elif(year%400==0):
    print("yes")
else:
    print("no")

