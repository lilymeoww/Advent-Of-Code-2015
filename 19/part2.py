with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

replacementRules = []
for line in inputRaw[:-2]:
    replacementRules.append((line[line.index(">")+1:].strip(), line[:line.index("=")-1].strip()))

stepCount = 0
currentMolecule = inputRaw[-1]

while currentMolecule != "e":
    for original, replacement in replacementRules:
        index = currentMolecule.find(original)
        if index != -1:
            currentMolecule = currentMolecule[:index] + replacement + currentMolecule[index+len(original):]
            stepCount += 1
            break

print(stepCount)