with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

lightsArray = [[0]*1000]*1000

def toggle(coord1X, coord1Y, coord2X, coord2Y, array):
    for xStep in range(coord2X-coord1X):
        for yStep in range(coord2Y-coord1Y):
            print(array[coord1Y + yStep][coord1X + xStep])
            if array[coord1Y + yStep][coord1X + xStep] == 0:
                array[coord1Y + yStep][coord1X + xStep] = 1
                # print(f"{coord1X+xStep},{coord1Y+yStep} toggled from 0 to 1.")
            elif array[coord1Y + yStep][coord1X + xStep] == 1:
                array[coord1Y + yStep][coord1X + xStep] = 0
                # print(f"{coord1X + xStep},{coord1Y + yStep} toggled from 1 to 0.")

def turnOn(coord1X, coord1Y, coord2X, coord2Y, array):
    pass

def turnOff(coord1X, coord1Y, coord2X, coord2Y, array):
    pass

toggle(0, 0, 100, 100, lightsArray)
print(lightsArray[99][99])
print(lightsArray[101][101])
# coord1X = coord1.split(",")[0]
# coord1Y = coord1.split(",")[1]
# coord2X = coord2.split(",")[0]
# coord2Y = coord2.split(",")[1]