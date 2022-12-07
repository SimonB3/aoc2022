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

def addSizeToDirectory(currentDirectories, directoriesAndSizes, resultLine):
    size = int(resultLine.split(' ')[0])
    for directory in currentDirectories:
        if directory in directoriesAndSizes:
            directoriesAndSizes[directory] += size
        else:
            directoriesAndSizes[directory] = size
    
def handleLs(addSizeToDirectory, currentDirectories, directoriesAndSizes, result):
    for resultLine in result.split('\n'):
        if not resultLine.startswith('dir') and resultLine != '':
            addSizeToDirectory(currentDirectories, directoriesAndSizes, resultLine)

rawtextString = loadRawData(getFileName())
commandSplittedData = rawtextString.split('$ ')[1:]
print(commandSplittedData)
commandResultPairs = [commandResult.split('\n', 1) for commandResult in commandSplittedData]
print(commandResultPairs)

currentDirectories = []
directoriesAndSizes = {}
for command, result in commandResultPairs:
    if(command.startswith('cd')):
        if(command.endswith('/')):
            currentDirectories = ['/']
        elif(command.endswith('..')):
            currentDirectories.pop()
        else:
            currentDirectories.append(currentDirectories[-1]+'/'+command[3:])
    elif(command == 'ls'):
        handleLs(addSizeToDirectory, currentDirectories, directoriesAndSizes, result)
        
print(sum([directorySize for directorySize in directoriesAndSizes.values() if directorySize <= 100000]))