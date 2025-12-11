with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

bossHitPoints = int(inputRaw[0].split(": ")[1])
bossDamage = int(inputRaw[1].split(": ")[1])
bossArmor = int(inputRaw[2].split(": ")[1])

weaponsForSale = {
    "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
    "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
    "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
    "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
    "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0}
}
armorForSale = {
    "None": {"Cost": 0, "Damage": 0, "Armor": 0},
    "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
    "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
    "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
    "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
    "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5}
}
ringsForSale = {
    "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
    "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
    "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
    "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
    "Defense +2": {"Cost": 40, "Damage": 0, "Armor": 2},
    "Defense +3": {"Cost": 80, "Damage": 0, "Armor": 3},
}

def simulateBattle(myDamage, myArmor, myCost, bossHitPoints, bossDamage, bossArmor):
    myHitPoints = 100
    currentTurn = "Player"

    while myHitPoints > 0 and bossHitPoints > 0:
        if currentTurn == "Player":
            bossHitPoints -= max((myDamage - bossArmor), 1)
            currentTurn = "Boss"
        else:
            myHitPoints -= max((bossDamage - myArmor), 1)
            currentTurn = "Player"

    return "Player" if bossHitPoints < 1 else "Boss"

possibleRingAmounts = [0, 1, 2]
myDamage = 0
myArmor = 0
myCost = 0

battlesWonCosts = []
for weapon in weaponsForSale:
    for armor in armorForSale:
        for amountOfRings in possibleRingAmounts:
            if amountOfRings == 0:
                myDamage = weaponsForSale[weapon]["Damage"]
                myArmor = armorForSale[armor]["Armor"]
                myCost = weaponsForSale[weapon]["Cost"] + armorForSale[armor]["Cost"]
                if simulateBattle(myDamage, myArmor, myCost, bossHitPoints, bossDamage, bossArmor) == "Boss":
                    battlesWonCosts.append(myCost)
            if amountOfRings == 1:
                for ring in ringsForSale:
                    myDamage = weaponsForSale[weapon]["Damage"] + ringsForSale[ring]["Damage"]
                    myArmor = armorForSale[armor]["Armor"] + ringsForSale[ring]["Armor"]
                    myCost = weaponsForSale[weapon]["Cost"] + armorForSale[armor]["Cost"] + ringsForSale[ring]["Cost"]
                    if simulateBattle(myDamage, myArmor, myCost, bossHitPoints, bossDamage, bossArmor) == "Boss":
                        battlesWonCosts.append(myCost)
            if amountOfRings == 2:
                for ring1 in ringsForSale:
                    ringsForSaleNow = ringsForSale.copy()
                    del ringsForSaleNow[ring1]
                    for ring2 in ringsForSaleNow:
                        myDamage = weaponsForSale[weapon]["Damage"] + ringsForSale[ring1]["Damage"] + ringsForSale[ring2]["Damage"]
                        myArmor = armorForSale[armor]["Armor"] + ringsForSale[ring1]["Armor"] + ringsForSale[ring2]["Armor"]
                        myCost = weaponsForSale[weapon]["Cost"] + armorForSale[armor]["Cost"] + ringsForSale[ring1]["Cost"] + ringsForSale[ring2]["Cost"]
                        if simulateBattle(myDamage, myArmor, myCost, bossHitPoints, bossDamage, bossArmor) == "Boss":
                            battlesWonCosts.append(myCost)


print(sorted(battlesWonCosts)[-1])