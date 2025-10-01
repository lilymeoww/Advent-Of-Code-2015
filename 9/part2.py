from itertools import permutations

with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

destinations = ["AlphaCentauri","Snowdin","Tambi","Faerun","Norrath","Straylight","Tristram", "Arbre"]

distances = {}
for line in inputRaw:
    city1 = line.split(" ")[0]
    city2 = line.split(" ")[2]
    distance = line.split(" ")[4]

    distances[(city1, city2)] = int(distance)

def checkDistance(city1, city2):
    if (city1, city2) in distances:
        return distances[(city1, city2)]
    else:
        return distances[(city2, city1)]

permutations = permutations(destinations)
routeLengths = []
for permutation in permutations:
    distance = 0
    for cityIndex in range(len(permutation)-1):
        distance += checkDistance(permutation[cityIndex], permutation[cityIndex+1])
    routeLengths.append(distance)


routeLengths.sort()
print(routeLengths[-1])


