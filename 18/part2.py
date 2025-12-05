with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()


directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
inputRaw = [list(line.strip()) for line in inputRaw]

for i in range(100):
    editQueue = []
    for rowIndex in range(len(inputRaw)):
        for columnIndex in range(len(inputRaw[0])):
            if inputRaw[rowIndex][columnIndex] == "#":
                neighbors = 0
                for dr, dc in directions:
                        checkingRow = rowIndex + dr
                        checkingColumn = columnIndex + dc
                        if 0 <= checkingRow < len(inputRaw) and 0 <= checkingColumn < len(inputRaw[0]):
                            if inputRaw[checkingRow][checkingColumn] == "#":
                                neighbors += 1
                if neighbors != 2 and neighbors != 3:
                    editQueue.append([rowIndex, columnIndex])
            elif inputRaw[rowIndex][columnIndex] == ".":
                neighbors = 0
                for dr, dc in directions:
                        checkingRow = rowIndex + dr
                        checkingColumn = columnIndex + dc
                        if 0 <= checkingRow < len(inputRaw) and 0 <= checkingColumn < len(inputRaw[0]):
                            if inputRaw[checkingRow][checkingColumn] == "#":
                                neighbors += 1
                if neighbors == 3:
                    editQueue.append([rowIndex, columnIndex])

    if editQueue:
        for row, column in editQueue:
            if inputRaw[row][column] == "#":
                inputRaw[row][column] = "."
            else:
                inputRaw[row][column] = "#"

    inputRaw[0][0] = "#"
    inputRaw[99][99] = "#"
    inputRaw[0][99] = "#"
    inputRaw[99][0] = "#"

onCount = 0
for rowIndex in range(len(inputRaw)):
    for columnIndex in range(len(inputRaw[0])):
        if inputRaw[rowIndex][columnIndex] == "#":
            onCount += 1

print(onCount)