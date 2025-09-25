with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

runningTotalString = 0
runningTotalNew = 0
for line in inputRaw:
    charCount = 0
    containsHex = True
    containsBackslash = True
    containsQuote = True

    runningTotalString += len(line)

    while containsQuote:
        if '"' in line[1:-1]:
            charCount += 1
            temp = line[1:-1].replace('\\\"', "", 1)
            line = '"' + temp + '"'
        else:
            containsQuote = False
    while containsBackslash:
        if '\\\\' in line[1:-1]:
            charCount += 1
            temp = line[1:-1].replace('\\\\', "", 1)
            line = '"' + temp + '"'
        else:
            containsBackslash = False
    while containsHex:
        if "\\x" in line[1:-1]:
            charCount += 1
            temp = line[1:-1].replace(line[1:-1][line[1:-1].find('\\x'):line[1:-1].find('\\x')+4], "", 1)
            line = '"' + temp + '"'
        else:
            containsHex = False

    runningTotalMemory += len(line)-2
    runningTotalMemory += charCount


print(runningTotalString-runningTotalMemory)

