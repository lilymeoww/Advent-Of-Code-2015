import re

with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

def sandwichCheck(string):
    for charIndex in range(len(string)):
        try:
            if string[charIndex] == string[charIndex+2]:
                return True
        except:
            return False

def repeatCheck(string):
    for charIndex in range(len(string)):
        try:
            if len(re.findall(string[charIndex] + string[charIndex+1], string)) > 1:
                print(string,string[charIndex] + string[charIndex+1])
                return True
        except:
            return False

niceCount = 0

for word in inputRaw:
    if sandwichCheck(word) and repeatCheck(word):
        niceCount += 1

print(niceCount)



