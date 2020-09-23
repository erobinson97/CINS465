import sys

vowels = ['a', 'e', 'i', 'o', 'u'] # consider adding 'y'
returnList = []

# Push lines into a list
text = sys.stdin.readlines()
temp = []
for x in text:
    x = x.rstrip("\n")
    x = x.lower()
    temp.append(x)

# Process list
for x in temp:
    if("-yay" in x):
        x = x[:-4]
        tempStr = x[0].upper() + x[1:]
        returnList.append(tempStr)
    else:
        index = 0
        consonant = ""
        afterDash = False
        beforeDash_subStr = ""

        for ch in x:
            if(ch != "-" and not afterDash):
                beforeDash_subStr = beforeDash_subStr + ch
                continue
            else:
                afterDash = True
                if(ch == "-"):
                    continue
                consonant = consonant + ch
        consonant = consonant[:-2]
        tempStr = consonant + beforeDash_subStr
        tempStr = tempStr[0].upper() + tempStr[1:]
        returnList.append(tempStr)

for x in returnList:
    print(x)