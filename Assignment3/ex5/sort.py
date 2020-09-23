import sys
msg = sys.stdin.readlines()
msg.sort()
for x in msg:
    x = x.rstrip("\n")
    print(x)