with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

boxes = []
for item in inputRaw:
    boxes.append(item.split("x"))

paperRequired = 0
for box in boxes:
    length = int(box[0])
    width = int(box[1])
    height = int(box[2])

    paperRequired += (2*length*width)
    paperRequired += (2*width*height)
    paperRequired += (2*length*height)

    side1 = length*width
    side2 = length*height
    side3 = height*width

    if side1 <= side2 and side1 <= side3:
        paperRequired += side1
    elif side2 <= side1 and side2 <= side3:
        paperRequired += side2
    else:
        paperRequired += side3

print(paperRequired)