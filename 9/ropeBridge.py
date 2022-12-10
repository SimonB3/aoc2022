import sys
import numpy as np

def loadMovelist(filename):
    directions = {'R': np.array([0, 1]), 'L': np.array([0, -1]), 'D': np.array([1, 0]), 'U': np.array([-1, 0])}
    movelist = []
    with open(filename) as file:
        for line in file.readlines():
            (direction, distance) = line.strip().split(' ')
            [movelist.append(directions[direction]) for i in range(int(distance))]
    
    return movelist

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

def calculateNewTailPos(headPos, tailPos):
    tailHeadDistance=headPos-tailPos
    if (abs(tailHeadDistance[0]) > 1):
        tailPos[0]+=np.sign(tailHeadDistance[0])
        if(abs(tailHeadDistance[1]) > 0):
            tailPos[1]+=np.sign(tailHeadDistance[1])
    elif (abs(tailHeadDistance[1]) > 1):
        tailPos[1]+=np.sign(tailHeadDistance[1])
        if(abs(tailHeadDistance[0]) > 0):
            tailPos[0]+=np.sign(tailHeadDistance[0])

  #  print(f"head: {headPos}, tail: {tailPos}, distance (before tail move): {tailHeadDistance}, distance (after tail move): {headPos-tailPos}")

    return tailPos

headPos = np.array([0, 0])
knotPos1 = np.array([0, 0])
knotPos2 = np.array([0, 0])
knotPos3 = np.array([0, 0])
knotPos4 = np.array([0, 0])
knotPos5 = np.array([0, 0])
knotPos6 = np.array([0, 0])
knotPos7 = np.array([0, 0])
knotPos8 = np.array([0, 0])
tailPos = np.array([0, 0])
tailVisitedPosition = set()
for move in loadMovelist(getFileName()):
    headPos+=move
    
    knotPos1 = calculateNewTailPos(headPos, knotPos1)
    knotPos2 = calculateNewTailPos(knotPos1, knotPos2)
    knotPos3 = calculateNewTailPos(knotPos2, knotPos3)
    knotPos4 = calculateNewTailPos(knotPos3, knotPos4)
    knotPos5 = calculateNewTailPos(knotPos4, knotPos5)
    knotPos6 = calculateNewTailPos(knotPos5, knotPos6)
    knotPos7 = calculateNewTailPos(knotPos6, knotPos7)
    knotPos8 = calculateNewTailPos(knotPos7, knotPos8)
    tailPos = calculateNewTailPos(knotPos8, tailPos)
    tailVisitedPosition.add((tailPos[0], tailPos[1]))

    

print(f"tail visited {len(tailVisitedPosition)} positions")