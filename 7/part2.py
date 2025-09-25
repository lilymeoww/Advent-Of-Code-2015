with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()

instructions = {}
wireValues = {}

for instruction in inputRaw:
    output = instruction.split("-> ")[1]
    if "LSHIFT" in instruction:
        operator = "LSHIFT"
        input1 = instruction.split(" ")[0]
        input2 = instruction.split(" ")[2]
    elif "RSHIFT" in instruction:
        operator = "RSHIFT"
        input1 = instruction.split(" ")[0]
        input2 = instruction.split(" ")[2]
    elif "AND" in instruction:
        operator = "AND"
        input1 = instruction.split(" ")[0]
        input2 = instruction.split(" ")[2]
    elif "OR" in instruction:
        operator = "OR"
        input1 = instruction.split(" ")[0]
        input2 = instruction.split(" ")[2]
    elif "NOT" in instruction:
        operator = "NOT"
        input1 = instruction.split(" ")[1]
        input2 = None
    else:
        operator = "VAL"
        input1 = instruction.split(" ")[0]
        input2 = None

    instructions[output] = (operator, input1, input2)
    instructions["b"] = ("VAL", "46065", None)
    wireValues[output] = None

def evaluate(wire):
    if wire.isdigit():
        return int(wire) & 0xFFFF
    elif wireValues[wire] != None:
        return int(wireValues[wire])&0xFFFF
    elif instructions[wire][0] == "VAL" and instructions[wire][1].isdigit():
        wireValues[wire] = int(instructions[wire][1])&0xFFFF
        return int(instructions[wire][1])&0xFFFF
    elif instructions[wire][0] == "VAL":
        wireValues[wire] = int(evaluate(instructions[wire][1]))&0xFFFF
        return int(evaluate(instructions[wire][1]))&0xFFFF
    elif instructions[wire][0] == "NOT":
        wireValues[wire] = ~int(evaluate(instructions[wire][1])) & 0xFFFF
        return ~int(evaluate(instructions[wire][1])) & 0xFFFF
    elif instructions[wire][0] == "AND":
        wireValues[wire] = int(int(evaluate(instructions[wire][1])) & 0xFFFF & int(evaluate(instructions[wire][2])) & 0xFFFF)&0xFFFF
        return int(int(evaluate(instructions[wire][1])) & 0xFFFF & int(evaluate(instructions[wire][2])) & 0xFFFF)&0xFFFF
    elif instructions[wire][0] == "OR":
        wireValues[wire] = int(int(evaluate(instructions[wire][1])) & 0xFFFF | int(evaluate(instructions[wire][2])) & 0xFFFF)&0xFFFF
        return int(int(evaluate(instructions[wire][1])) & 0xFFFF | int(evaluate(instructions[wire][2])) & 0xFFFF)&0xFFFF
    elif instructions[wire][0] == "LSHIFT":
        wireValues[wire] = int(int(evaluate(instructions[wire][1]))<< int(instructions[wire][2]))&0xFFFF
        return int(int(evaluate(instructions[wire][1])) << int(instructions[wire][2]))&0xFFFF
    elif instructions[wire][0] == "RSHIFT":
        wireValues[wire] = int(int(evaluate(instructions[wire][1])) >> int(instructions[wire][2]))&0xFFFF
        return int(int(evaluate(instructions[wire][1])) >> int(instructions[wire][2]))&0xFFFF


print(evaluate("a"))
