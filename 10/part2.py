number = "1321131112"

for i in range(50):
    print(i)
    result = []
    numberArr = list(number)
    countNumbers = 0
    for numberIndex in range(len(numberArr)):
        if numberIndex == 0:
            countNumbers += 1
        elif numberArr[numberIndex] == numberArr[numberIndex-1]:
            countNumbers += 1
        else:
            result.append(str(countNumbers))
            result.append(numberArr[numberIndex-1])
            countNumbers = 1
    number = "".join(result) + str(countNumbers) + numberArr[-1]

print(len(number))

