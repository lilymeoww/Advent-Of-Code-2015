with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

ingredients = {}
for line in inputRaw:
    ingredients[line.split(":")[0]] = (int(line.split(" ")[2].strip(",")),
                                       int(line.split(" ")[4].strip(",")),
                                       int(line.split(" ")[6].strip(",")),
                                       int(line.split(" ")[8].strip(",")),
                                       int(line.split(" ")[10].strip(",")))


combinations = []
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            l = 100 - i - j - k
            combinations.append([i, j, k, l])

cookieScores = []

for possibility in combinations:
    capacity = durability = flavor = texture = calories = 0
    for ingredientIndex in range(len(possibility)):
        capacity += possibility[ingredientIndex] * ingredients[str(ingredientIndex)][0]
        durability += possibility[ingredientIndex] * ingredients[str(ingredientIndex)][1]
        flavor += possibility[ingredientIndex] * ingredients[str(ingredientIndex)][2]
        texture += possibility[ingredientIndex] * ingredients[str(ingredientIndex)][3]
        calories += possibility[ingredientIndex] * ingredients[str(ingredientIndex)][4]
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    calories = max(0, calories)
    if calories == 500:
        cookieScores.append(capacity*durability*flavor*texture)

print(max(cookieScores))

