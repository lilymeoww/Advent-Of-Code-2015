number = "1321131112"

for i in range(40):
    print(i)
    newString = ""
    numberArr = list(number)
    countNumbers = 0
    for numberIndex in range(len(numberArr)):
        if numberIndex == 0:
            countNumbers += 1
        elif numberArr[numberIndex] == numberArr[numberIndex-1]:
            countNumbers += 1
        else:
            newString += str(countNumbers) + numberArr[numberIndex-1]
            countNumbers = 1
    number = newString + str(countNumbers) + numberArr[-1]

print(len(number))

