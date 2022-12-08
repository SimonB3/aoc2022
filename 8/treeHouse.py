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

def singleDirectionViewingDistance(row, viewheight):
    score = 0
    for treeheight in row:
        score += 1
        if treeheight >= viewheight:
            break
    return score

def scenicScore(treeArray, row, column):
    viewHeight = treeArray[row, column]
    viewDistanceRight = singleDirectionViewingDistance(treeArray[row, column+1:], viewHeight)
    viewDistanceLeft = singleDirectionViewingDistance(np.flip(treeArray[row, :column]), viewHeight)
    viewDistanceUp = singleDirectionViewingDistance(np.flip(treeArray[:row, column]), viewHeight)
    viewDistanceDown = singleDirectionViewingDistance(treeArray[row+1:, column], viewHeight)
    return viewDistanceLeft * viewDistanceRight * viewDistanceUp * viewDistanceDown

treeArray = loadNumpyArray(getFileName())

visibleFromLeft = np.apply_along_axis(visibleInList, 1, treeArray)
visibleFromRight = np.fliplr(np.apply_along_axis(visibleInList, 1, np.fliplr(treeArray)))
visibleFromTop = np.apply_along_axis(visibleInList, 0, treeArray)
visibleFromBottom = np.flipud(np.apply_along_axis(visibleInList, 0, np.flipud(treeArray)))

visibleFromAnyDirection = np.logical_or(np.logical_or(visibleFromLeft, visibleFromRight), np.logical_or(visibleFromTop, visibleFromBottom))

print(np.count_nonzero(visibleFromAnyDirection))
print(max([scenicScore(treeArray, indices[0][0], indices[0][1]) for indices in np.ndenumerate(treeArray)]))
