import sys
import numpy as np

def loadNumpyArray(filename):
    
    with open(filename) as file:
        lineList = []
        for line in file.readlines():
            lineList.append(list(line.strip()))
    return np.array(lineList)


    return contents

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

def visibleInList(inputlist):
    isVisible = []
    obstacleHeight = -1
    for height in inputlist:
        if int(height) > obstacleHeight:
            isVisible.append(True)
            obstacleHeight = int(height)
        else:
            isVisible.append(False)
    return isVisible

treeArray = loadNumpyArray(getFileName())
print(treeArray)

visibleFromLeft = np.apply_along_axis(visibleInList, 1, treeArray)
visibleFromRight = np.fliplr(np.apply_along_axis(visibleInList, 1, np.fliplr(treeArray)))
visibleFromTop = np.apply_along_axis(visibleInList, 0, treeArray)
visibleFromBottom = np.flipud(np.apply_along_axis(visibleInList, 0, np.flipud(treeArray)))

visibleFromAnyDirection = np.logical_or(np.logical_or(visibleFromLeft, visibleFromRight), np.logical_or(visibleFromTop, visibleFromBottom))

print(visibleFromAnyDirection)

print(np.count_nonzero(visibleFromAnyDirection))