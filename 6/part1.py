with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

lightsArray = [[0]*1000 for _ in range(1000)]

def toggle(coord1X, coord1Y, coord2X, coord2Y):
    for deltaX in range((coord2X-coord1X)+1):
        for deltaY in range((coord2Y-coord1Y)+1):
            if lightsArray[coord1Y+deltaY][coord1X+deltaX] == 1:
                lightsArray[coord1Y+deltaY][coord1X+deltaX] = 0
                # print(f"({coord1X+deltaX},{coord1Y+deltaY}) toggled to 0.")
            elif lightsArray[coord1Y+deltaY][coord1X+deltaX] == 0:
                lightsArray[coord1Y+deltaY][coord1X+deltaX] = 1
                # print(f"({coord1X + deltaX},{coord1Y + deltaY}) toggled to 1.")


def turnOn(coord1X, coord1Y, coord2X, coord2Y):
    for deltaX in range((coord2X-coord1X)+1):
        for deltaY in range((coord2Y-coord1Y)+1):
            lightsArray[coord1Y+deltaY][coord1X+deltaX] = 1


def turnOff(coord1X, coord1Y, coord2X, coord2Y):
    for deltaX in range((coord2X-coord1X)+1):
        for deltaY in range((coord2Y-coord1Y)+1):
            lightsArray[coord1Y+deltaY][coord1X+deltaX] = 0

for instruction in inputRaw:
    if "turn off" in instruction:
        turnOff(int(instruction.split(" ")[2].split(",")[0]),
                int(instruction.split(" ")[2].split(",")[1]),
                int(instruction.split(" ")[4].split(",")[0]),
                int(instruction.split(" ")[4].split(",")[1]))
    elif "turn on" in instruction:
        turnOn(int(instruction.split(" ")[2].split(",")[0]),
                int(instruction.split(" ")[2].split(",")[1]),
                int(instruction.split(" ")[4].split(",")[0]),
                int(instruction.split(" ")[4].split(",")[1]))
    elif "toggle" in instruction:
        toggle(int(instruction.split(" ")[1].split(",")[0]),
                int(instruction.split(" ")[1].split(",")[1]),
                int(instruction.split(" ")[3].split(",")[0]),
                int(instruction.split(" ")[3].split(",")[1]))

onCount = 0
for row in lightsArray:
    for light in row:
        if light == 1:
            onCount += 1

print(onCount)