with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()
doubleLetters = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy","zz"]
vowels = {"a", "e", "i", "o", "u"}
niceCount = 0
for string in inputRaw:
    failedDoubleCheck = False
    failedVowelCheck = True
    failedSpecificCheck = True
    for doubleLetter in doubleLetters:
        if doubleLetter in string:
            pass
        elif doubleLetter == "zz" and doubleLetter not in string:
            failedDoubleCheck = True
    if not failedDoubleCheck:
        if "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string:
            failedSpecificCheck = False
        if not failedSpecificCheck:
            failedVowelCheck = True
            if sum(1 for char in string if char in vowels) >=3:
                failedVowelCheck = False

    if not failedSpecificCheck and not failedVowelCheck and not failedDoubleCheck:
        niceCount += 1

print(niceCount)

