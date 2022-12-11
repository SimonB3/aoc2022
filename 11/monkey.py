import sys
import re
import ast
import numpy as np

class Monkey:
    def __init__(self, datastring) -> None:
        self.rawData = datastring
        self.parseStartItems()
        self.parseDivisibility()
        self.parseTargetMonkeys()
        self.parseOperation()
        self.inspectedItems = 0

    def parseStartItems(self):
        regex = re.search('Starting items: (.+)\n', self.rawData)
        startItemsString = regex.group(1)
        self.items = [int(item) for item in startItemsString.split(', ')]

    def parseDivisibility(self):
        regex = re.search('Test: divisible by (.+)\n', self.rawData)
        self.divisibility = int(regex.group(1))

    def parseTargetMonkeys(self):
        regex = re.search('If true: throw to monkey (.+)\n', self.rawData)
        self.trueTarget = int(regex.group(1))
        regex = re.search('If false: throw to monkey (.+)\n', self.rawData)
        self.falseTarget = int(regex.group(1))

    def parseOperation(self):
        regex = re.search('Operation: new = (.+)\n', self.rawData)
        self.operation = ast.parse(regex.group(1), mode='eval')

    def throwThings(self):
        thrownlist = [self.determineThrow(thing) for thing in self.items]
        self.items = []
        return thrownlist

    def determineThrow(self, thing):
        old = thing
        newValue = eval(compile(self.operation, '', mode='eval'))//3
        self.inspectedItems += 1
        if (newValue % self.divisibility) == 0:
            target = self.trueTarget
        else:
            target = self.falseTarget
        return(target, newValue)


    def __str__(self) -> str:
         return f"Current items: {self.items}\nOperation:{ast.dump(self.operation)}\nDivisibility: {self.divisibility}\nIf true throw to: {self.trueTarget}\nIf false throw to: {self.falseTarget}"


def loadMonkeys(filename):
    with open(filename) as file:
        monkeyList = []
        fullFile = file.read()
    
    for monkeyData in re.split('Monkey .:\n', fullFile)[1:]:
            currentMonkey = Monkey(monkeyData)
            print(currentMonkey)
            monkeyList.append(currentMonkey)
    return monkeyList

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

allMonkeydata = loadMonkeys(getFileName())

for round in range(20):
    for monkey in allMonkeydata:
        thrownthings = monkey.throwThings()
        for (target, item) in thrownthings:
            allMonkeydata[target].items.append(item)

inspectedItems = [monkey.inspectedItems for monkey in allMonkeydata]
inspectedItems.sort(reverse=True)
print(np.prod(inspectedItems[0:2]))