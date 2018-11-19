a=raw_input()
"""if all(b in '01' for b in a):
    print "yes"
else:
    print "no"
    """
if not(a.translate(None,'01')):
    print "yes"
else:
    print "no"



