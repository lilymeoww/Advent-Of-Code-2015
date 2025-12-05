presentGoal = 34000000

maxId = 2
complete = False
while not complete:
    houses = [0] * (maxId + 1)
    for elf in range(1, maxId):
        for multiple in range(elf, maxId + 1, elf):
            houses[multiple] += 10 * elf

    for house in range(1, maxId + 1):
        if houses[house] >= presentGoal:
            print(house)
            complete = True
            break

    maxId *= 2
