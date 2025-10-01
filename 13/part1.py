from itertools import permutations

with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

peopleNames = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]
happinessChanges = {}
for line in inputRaw:
    person1 = line.split(" ")[0]
    person2 = line.split(" ")[-1].strip(".").strip()
    change = int(line.split(" ")[3])
    polarity = "n" if line.split(" ")[2] == "lose" else "p"

    happinessChanges[(person1, person2)] = -1*change if polarity == "n" else change

possibleLayoutScores = []

for permutation in permutations(peopleNames):
    print(permutation)
    permutationScore = 0
    for personIndex in range(len(peopleNames)-1):
        permutationScore += happinessChanges[(permutation[personIndex], permutation[personIndex+1])]
        permutationScore += happinessChanges[(permutation[personIndex+1], permutation[personIndex])]
    permutationScore += happinessChanges[(permutation[0], permutation[-1])]
    permutationScore += happinessChanges[(permutation[-1], permutation[0])]
    possibleLayoutScores.append(permutationScore)


possibleLayoutScores.sort()
print(possibleLayoutScores)
print(possibleLayoutScores[-1])


