presentGoal = 34000000

maxId = 2
complete = False
while not complete:
    houses = [0] * (maxId + 1)
    for elf in range(1, maxId):
        for multiplier in range(1, 51):
            house = elf * multiplier
            if house > maxId:#
                break
            houses[house] += 11 * elf

    for house in range(1, maxId + 1):
        if houses[house] >= presentGoal:
            print(house)
            complete = True
            break

    maxId *= 2
