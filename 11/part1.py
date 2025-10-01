from anyio import current_effective_deadline

currentPassword = "cqjxjnds"

def increment(currentPassword):
    newString = ""
    for character in currentPassword:
        if character != "z":
            newString += chr(ord(character)+1)
        else:
            newString += "a"
    return newString


valid = False

while not valid:
    currentPassword = increment(currentPassword)
    iolCheckPass = False
    doubleLettersCheckPass = False
    runsCheckPass = False
    if "i" not in currentPassword and "o" not in currentPassword and "l" not in currentPassword:
        iolCheckPass  = True
    if iolCheckPass:
        # check for double letters
        pass
    if doubleLettersCheckPass:
        # check for runs
        pass
    if runsCheckPass:
        valid = True
        print(currentPassword)