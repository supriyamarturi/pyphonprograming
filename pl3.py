num = int(raw_input())    
Rev = 0    
while(num > 0):    
    Reminder = num %10    
    Rev = (Rev *10) + Reminder    
    num = num //10    
     
print Rev   
