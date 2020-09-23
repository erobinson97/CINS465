import sys
text = sys.stdin.readlines()
temp = []
for x in text:
    if(x not in temp):
        temp.append(x)
for x in temp:
    x = x.rstrip("\n")
    print(x)