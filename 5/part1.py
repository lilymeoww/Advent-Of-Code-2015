with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

specificCombos = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]

def doubleLettersCheck(string):
    temp = ""
    failed = False
    for char in string:
        if char == temp:
            failed = True
            print(f"found double!! word: {string}")
            return True # Failed
        temp = char
    if not failed:
        return False

def specificComboCheck(string):
    failed = False
    for combo in specificCombos:
        if combo in string:
            failed = True
            return False
    if not failed:
        return True

def threeVowelCheck(string):
    vowelCount = 0
    for char in string:
        for vowel in vowels:
            if char == vowel:
                vowelCount += 1
    if vowelCount >= 3:
        return True
    else:
        return False

niceCount = 0

for word in inputRaw:
    if threeVowelCheck(word) and specificComboCheck(word) and doubleLettersCheck(word):
        niceCount += 1

print(niceCount)



