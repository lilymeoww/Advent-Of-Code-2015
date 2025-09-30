with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

runningTotalString = 0
runningTotalNew = 0
for line in inputRaw:
    newString = ""
    for char in line:
        if char == '"':
            newString += '\\"'
        elif char ==  '\\':
            newString += '\\\\'
        else:
            newString += char

    newString = '"' + newString + '"'

    runningTotalNew += len(newString)
    runningTotalString += len(line)
    print(newString)

print(runningTotalNew-runningTotalString)





