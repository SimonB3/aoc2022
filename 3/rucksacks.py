import sys

def loadRucksacks(filename):
    allRucksacks = []
    with open(filename) as file:
        for line in file.readlines():
            strippedLine = line.strip()
            allRucksacks.append((set(strippedLine[:len(strippedLine)//2]), set(strippedLine[len(strippedLine)//2:])))

    return allRucksacks

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

def itemValue(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

allRucksacks = loadRucksacks(getFileName())
commonItems = [compartments[0].intersection(compartments[1]) for compartments in allRucksacks]
commonItemsPriority = [itemValue(item.pop()) for item in commonItems]
print(sum(commonItemsPriority))