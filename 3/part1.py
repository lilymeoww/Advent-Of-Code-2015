with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

xPos = 0
yPos = 0
visitedHouses = [[0,0]]

for instruction in inputRaw[0]:
    if instruction == ">":
         xPos += 1
         if [xPos, yPos] not in visitedHouses:
             visitedHouses.append([xPos, yPos])
    elif instruction == "<":
         xPos -= 1
         if [xPos, yPos] not in visitedHouses:
             visitedHouses.append([xPos, yPos])
    elif instruction == "^":
        yPos += 1
        if [xPos, yPos] not in visitedHouses:
            visitedHouses.append([xPos, yPos])
    elif instruction == "v":
        yPos -= 1
        if [xPos, yPos] not in visitedHouses:
            visitedHouses.append([xPos, yPos])

print(len(visitedHouses))
