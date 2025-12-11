with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

bossHitPoints = int(inputRaw[0].split(": ")[1])
bossDamage = int(inputRaw[1].split(": ")[1])

spellsAvailable = {
    "Magic Missile": {"Cost": 53, "Damage": 4, "Health": 0, "Armor": 0,  "Money": 0},
    "Drain": {"Cost": 73, "Damage": 2, "Health": 2, "Armor": 0,  "Money": 0},
    "Shield": {"Cost": 113, "Damage": 0, "Health": 0, "Armor": 7,  "Money": 0,  "Turns": 6},
    "Poison": {"Cost": 173, "Damage": 3, "Health": 0, "Armor": 0,  "Money": 0, "Turns": 6},
    "Recharge": {"Cost": 229, "Damage": 0, "Health": 0, "Armor": 0, "Money": 101, "Turns": 5}
}

possible
