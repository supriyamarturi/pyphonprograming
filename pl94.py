import sys,string, math,itertools
p = raw_input()
for d in p :
    if p.count(d) > 1 :
        print('yes')
        sys.exit()
print('no')






