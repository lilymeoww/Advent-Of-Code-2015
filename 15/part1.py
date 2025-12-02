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


