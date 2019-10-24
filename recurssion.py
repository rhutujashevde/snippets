import sys
sys.setrecursionlimit(15)
count= 0
def recurssion(count):
    count += 1
    print count
    recurssion(count)

recurssion(count)