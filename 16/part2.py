with open("input.txt", "r") as inputFile:
    inputRaw = inputFile.readlines()
    for lineIndex in range(len(inputRaw)):
        inputRaw[lineIndex] = inputRaw[lineIndex].strip()


for aunt in inputRaw:
    childrenPassed = catsPassed = samoyedsPassed = pomeraniansPassed = akitasPassed = vizslasPassed = goldfishPassed = treesPassed = carsPassed = perfumesPassed = False

    if "children" in aunt:
        if int(aunt[aunt.find("children"):].split(",")[0].split(" ")[1].strip(",").strip()) == 3:
            childrenPassed = True
    else:
        childrenPassed = True

    if "cats" in aunt:
        if int(aunt[aunt.find("cats"):].split(",")[0].split(" ")[1].strip(",").strip()) > 7:
            catsPassed = True
    else:
        catsPassed = True

    if "samoyeds" in aunt:
        if int(aunt[aunt.find("samoyeds"):].split(",")[0].split(" ")[1].strip(",").strip()) == 2:
            samoyedsPassed = True
    else:
        samoyedsPassed = True

    if "pomeranians" in aunt:
        if int(aunt[aunt.find("pomeranians"):].split(",")[0].split(" ")[1].strip(",").strip()) < 4:
            pomeraniansPassed = True
    else:
        pomeraniansPassed = True

    if "akitas" in aunt:
        if int(aunt[aunt.find("akitas"):].split(",")[0].split(" ")[1].strip(",").strip()) == 0:
            akitasPassed = True
    else:
        akitasPassed = True

    if "vizslas" in aunt:
        if int(aunt[aunt.find("vizslas"):].split(",")[0].split(" ")[1].strip(",").strip()) == 0:
            vizslasPassed = True
    else:
        vizslasPassed = True

    if "goldfish" in aunt:
        if int(aunt[aunt.find("goldfish"):].split(",")[0].split(" ")[1].strip(",").strip()) < 5:
            goldfishPassed = True
    else:
        goldfishPassed = True

    if "trees" in aunt:
        if int(aunt[aunt.find("trees"):].split(",")[0].split(" ")[1].strip(",").strip()) > 3:
            treesPassed = True
    else:
        treesPassed = True

    if "cars" in aunt:
        if int(aunt[aunt.find("cars"):].split(",")[0].split(" ")[1].strip(",").strip()) == 2:
            carsPassed = True
    else:
        carsPassed = True

    if "perfumes" in aunt:
        if int(aunt[aunt.find("perfumes"):].split(",")[0].split(" ")[1].strip(",").strip()) == 1:
            perfumesPassed = True
    else:
        perfumesPassed = True

    if childrenPassed == catsPassed == samoyedsPassed == pomeraniansPassed == akitasPassed == vizslasPassed == goldfishPassed == treesPassed == carsPassed == perfumesPassed == True:
        print(aunt)
