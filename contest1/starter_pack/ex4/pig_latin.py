import sys

vowels = ['a', 'e', 'i', 'o', 'u'] # consider adding 'y'

text = sys.stdin.readlines()
temp = []
returnList = []
for x in text:
    x = x.rstrip("\n")
    x = x.lower()
    temp.append(x)

for x in temp:
    if((x[0]) in vowels):
        x = x + "-yay"
        returnList.append(x)
    else:
        consonant = ""
        index = 0
        for ch in x:
            if(ch not in vowels):
                consonant = consonant + ch
                index += 1
            else:
                break
        x = x[index:] + "-" + consonant + "ay"
        returnList.append(x)

for x in returnList:
    print(x)