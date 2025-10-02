with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

reindeerStates = {}
reindeerPositions = {}

for line in inputRaw:
    reindeerName = line.split(" ")[0]
    reindeerSpeed = int(line.split(" ")[3])
    reindeerStamina = int(line.split(" ")[6])
    reindeerRest = int(line.split(" ")[13])
    reindeerStates[reindeerName] = [reindeerSpeed for _ in range(reindeerStamina)] + [0 for _ in range(reindeerRest)]
    reindeerPositions[reindeerName] = [0, 0, reindeerStamina+reindeerRest]

currentTime = 0

while currentTime != 2503:
    for reindeer in reindeerPositions:
        reindeerPositions[reindeer][1] += reindeerStates[reindeer][reindeerPositions[reindeer][0]]
        if reindeerPositions[reindeer][0] == reindeerPositions[reindeer][2]-1:
            reindeerPositions[reindeer][0] = 0
        else:
            reindeerPositions[reindeer][0] += 1
    currentTime += 1

print(reindeerPositions)
