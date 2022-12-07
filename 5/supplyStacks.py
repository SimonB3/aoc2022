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
    numberToMove = int(move[0])
    cratesToMove = stacks[move[1]][-(numberToMove):]
    del stacks[move[1]][-(numberToMove):]
    stacks[move[2]].extend(cratesToMove)

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