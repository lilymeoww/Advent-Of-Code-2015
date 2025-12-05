with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

replacementRules = []
for line in inputRaw[:-2]:
    replacementRules.append((line[:line.index("=")-1].strip(), line[line.index(">")+1:].strip()))

possibleResults = set()
for original, replacement in replacementRules:
    indexTracker = 0
    while True:
        currentIndex = inputRaw[-1].find(original, indexTracker)
        if currentIndex == -1:
            break

        replacementString = inputRaw[-1][:currentIndex] + replacement + inputRaw[-1][currentIndex + len(original):]
        possibleResults.add(replacementString)
        indexTracker = currentIndex + 1

print(len(possibleResults))