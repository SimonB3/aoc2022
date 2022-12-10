import sys
import numpy as np

def loadOperations(filename):
    with open(filename) as file:
        lineList = []
        for line in file.readlines():
            lineList.append(line.strip().split(' '))
    return lineList

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

operations = loadOperations(getFileName())
print(operations)

registerValues = [1]
for operation in operations:
    registerValues.append(registerValues[-1])
    if operation[0] == 'addx':
        registerValues.append(registerValues[-1]+int(operation[1]))

print(registerValues)
signalStrength = 0
for index, regvalue in enumerate(registerValues):
    if (index-19) % 40 == 0:
        print(f"{index+1}:{regvalue}:{(index + 1)*regvalue}")
        signalStrength += (index+1)*regvalue

print(signalStrength)
    