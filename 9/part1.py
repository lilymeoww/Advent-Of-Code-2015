with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

distances = {}
for line in inputRaw:
    city1 = line.split(" ")[0]
    city2 = line.split(" ")[2]
    distance = line.split
