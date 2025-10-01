currentPassword = "cqjxxyzz"


def increment(currentPassword):
    chars = list(currentPassword)
    for i in range(len(chars) - 1, -1, -1):
        if chars[i] != 'z':
            chars[i] = chr(ord(chars[i]) + 1)
            break
        else:
            chars[i] = 'a'
    return ''.join(chars)



doubleLetters = ["aa", "bb", "cc", "dd", "ee",
                 "ff", "gg", "hh", "ii", "jj",
                 "kk", "ll", "mm", "nn", "oo",
                 "pp", "qq", "rr", "ss", "tt",
                 "uu", "vv", "ww", "xx", "yy", "zz"]

runs = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi",
        "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop",
        "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw",
        "vwx", "wxy", "xyz"]

valid = False

while not valid:
    currentPassword = increment(currentPassword)
    iolCheckPass = False
    doubleLettersCheckPass = False
    runsCheckPass = False
    if "i" not in currentPassword and "o" not in currentPassword and "l" not in currentPassword:
        iolCheckPass  = True
    if iolCheckPass:
        doublesCount = 0
        for pair in doubleLetters:
            if pair in currentPassword:
                doublesCount += 1
        if doublesCount >= 2:
            doubleLettersCheckPass = True
    if doubleLettersCheckPass:
        for run in runs:
            if run in currentPassword:
                runsCheckPass = True
    if runsCheckPass:
        valid = True
        print(currentPassword)