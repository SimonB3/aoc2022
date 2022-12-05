import sys, re

def loadRawData(filename):
    
    with open(filename) as file:
        contents = file.read()

    return contents

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

def makeStacks(stacksData):
    linelist = stacksData.split('\n')
    cratenumbering = linelist[-1]
    crateNumber = {index:number for index, number in enumerate(cratenumbering) if number.isdigit()}
    stacksDict = {index:[] for index in crateNumber.values()}
 
    for line in reversed(linelist[0:-1]):
        crateposition = {crateNumber[index]: number for index, number in enumerate(line) if number.isalpha()}
        for index, item in crateposition.items():
            stacksDict[index].append(item)
        
    return stacksDict

def parseMove(moveString):
    regexpMatch = re.search('move (.+) from (.+) to (.+)', moveString)
    numberOfCrates = regexpMatch.group(1)
    startStack = regexpMatch.group(2)
    targetStack = regexpMatch.group(3)
    return (numberOfCrates, startStack, targetStack)

def makeMove(stacks, move):
    for movenumber in range(int(move[0])):
        crateToMove = stacks[move[1]].pop(-1)
        stacks[move[2]].append(crateToMove)

rawInputData = loadRawData(getFileName())
(stacksData, moveData) = rawInputData.split('\n\n')
print(stacksData)
print('.....')
print(moveData)
stacks = makeStacks(stacksData)
moveList = [parseMove(moveString) for moveString in moveData.split('\n') if moveString != '']

for move in moveList:
    makeMove(stacks, move)
    
for stack in stacks.values():
    print(stack[-1])