# find duplicates
a = [1,2,5,3,4,4]

for i in a:
    if a.count(i) == 2:
        print i
        break

# not in second set
a=[1,2,3,4]
b=[2,3,4,5]
for i in a:
     if i not in b:
        print i

# ascii
 asciic= 66

for i in range(1,5):
    asciic -= 1
    for j in range(1,i+1):
        print chr(asciic),
        asciic += 1
    print ""