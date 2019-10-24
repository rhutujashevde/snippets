a = int(input("Enter a num"))

r = (a-1)/2

for i in reversed(range(1,r+1)):
    b = a-(i*2)
    print(("- "*i) + ("* "*b) + ("- "*i))
for i in range(2,r+1):
    b = a-(i*2)
    print(("- "*i) + ("* "*b) + ("- "*i))