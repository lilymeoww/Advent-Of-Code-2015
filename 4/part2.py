import hashlib

inputStr = "bgvyzdsv"
# inputStr = "abcdef"
num = 0
solved = False
while not solved:
    hashAttempt = hashlib.md5(f"{inputStr}{str(num)}".encode()).hexdigest()
    num+=1
    if hashAttempt[:6] == "000000":
        print(num-1)
        solved = True