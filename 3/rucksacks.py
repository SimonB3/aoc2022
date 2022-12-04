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

def itemPriority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

def uncompartmentalize(rucksacksWithCompartments):
    return [compartments[0].union(compartments[1]) for compartments in allRucksacks]

def makeGroupsOfThree(fullRucksacks):
    groupsOfThree = []
    for index in range(0, len(fullRucksacks)-2, 3):
        groupsOfThree.append([fullRucksacks[index], fullRucksacks[index+1], fullRucksacks[index+2]])

    return groupsOfThree

allRucksacks = loadRucksacks(getFileName())
commonItems = [compartments[0].intersection(compartments[1]) for compartments in allRucksacks]
commonItemsPriority = [itemPriority(item.pop()) for item in commonItems]
print(sum(commonItemsPriority))
groupedRucksacks = makeGroupsOfThree(uncompartmentalize(allRucksacks))
commonItemsInGroup = [rucksackGroup[0].intersection(rucksackGroup[1]).intersection(rucksackGroup[2]) for rucksackGroup in groupedRucksacks]
commonItemsInGroupPriority = [itemPriority(item.pop()) for item in commonItemsInGroup]
print(sum(commonItemsInGroupPriority))
