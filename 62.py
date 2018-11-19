n=raw_input()
"""if all(c in '01' for c in n):
    print "yes"
else:
    print "no"
    """
if not(n.translate(None,'01')):
    print "yes"
else:
    print "no"
