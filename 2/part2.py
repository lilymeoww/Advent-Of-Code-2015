with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

boxes = []
for item in inputRaw:
    boxes.append(item.split("x"))

ribbonRequired = 0
for box in boxes:
    length = int(box[0])
    width = int(box[1])
    height = int(box[2])

    if length >= width and length >= height:
        ribbonRequired += 2*width
        ribbonRequired += 2*height
    elif width >= length and width >= height:
        ribbonRequired += 2*length
        ribbonRequired += 2*height
    else:
        ribbonRequired += 2*length
        ribbonRequired += 2*width

    ribbonRequired += width*height*length
print(ribbonRequired)