with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

santaXPos = 0
santaYPos = 0
roboXPos = 0
roboYPos = 0
santaVisitedHouses = [[0,0]]
roboVisitedHouses = [[0,0]]

for instructionIndex in range(len(inputRaw[0])):
    if instructionIndex % 2 == 0:
        print(inputRaw[0][instructionIndex])
        if inputRaw[0][instructionIndex] == ">":
             santaXPos += 1
             if [santaXPos, santaYPos] not in santaVisitedHouses:
                 santaVisitedHouses.append([santaXPos, santaYPos])
        elif inputRaw[0][instructionIndex] == "<":
             santaXPos -= 1
             if [santaXPos, santaYPos] not in santaVisitedHouses:
                 santaVisitedHouses.append([santaXPos, santaYPos])
        elif inputRaw[0][instructionIndex] == "^":
            santaYPos += 1
            if [santaXPos, santaYPos] not in santaVisitedHouses:
                santaVisitedHouses.append([santaXPos, santaYPos])
        elif inputRaw[0][instructionIndex] == "v":
            santaYPos -= 1
            if [santaXPos, santaYPos] not in santaVisitedHouses:
                santaVisitedHouses.append([santaXPos, santaYPos])
    elif instructionIndex % 2 == 1:
        if inputRaw[0][instructionIndex] == ">":
             roboXPos += 1
             if [roboXPos, roboYPos] not in santaVisitedHouses:
                 santaVisitedHouses.append([roboXPos, roboYPos])
        elif inputRaw[0][instructionIndex] == "<":
             roboXPos -= 1
             if [roboXPos, roboYPos] not in santaVisitedHouses:
                 santaVisitedHouses.append([roboXPos, roboYPos])
        elif inputRaw[0][instructionIndex] == "^":
            roboYPos += 1
            if [roboXPos, roboYPos] not in santaVisitedHouses:
                santaVisitedHouses.append([roboXPos, roboYPos])
        elif inputRaw[0][instructionIndex] == "v":
            roboYPos -= 1
            if [roboXPos, roboYPos] not in santaVisitedHouses:
                santaVisitedHouses.append([roboXPos, roboYPos])

print(santaVisitedHouses)
print(roboVisitedHouses)
print(len(santaVisitedHouses)+len(roboVisitedHouses)-1)
