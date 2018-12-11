data =  raw_input().split(" ")
print "".join([kk for kk in data if data.count(kk) == 1])
