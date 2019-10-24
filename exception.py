a = [1,3,4,5,0,4,6,0,3,2,45,6,2]

for i in a:
    try:
        print i, 1/i
    except ZeroDivisionError:
        print "rhutuja"
        continue