with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

floorInstructions = inputRaw[0]

floor = 0
instructionIndex = 0

for instruction in floorInstructions:
    instructionIndex += 1
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1

    if floor < 0:
        print(instructionIndex)
        break