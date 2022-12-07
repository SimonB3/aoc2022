import sys

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

rawtextString = loadRawData(getFileName())

for index in range(13,len(rawtextString)):
    partToCheck = rawtextString[index-14:index]
    if len(set(partToCheck)) == 14:
        break

print(index)