with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

floorInstructions = inputRaw[0]

floor = 0

for instruction in floorInstructions:
    if instruction == "(":
        floor += 1
    else:
        floor -= 1

print(floor)