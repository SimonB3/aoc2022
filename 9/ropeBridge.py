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

headPos = np.array([0, 0])
tailPos = np.array([0, 0])
tailVisitedPosition = set()
for move in loadMovelist(getFileName()):
    headPos+=move
    
    tailHeadDistance=headPos-tailPos
    if (abs(tailHeadDistance[0]) > 1):
        tailPos[0]+=np.sign(tailHeadDistance[0])
        if(abs(tailHeadDistance[1]) > 0):
            tailPos[1]+=np.sign(tailHeadDistance[1])
    elif (abs(tailHeadDistance[1]) > 1):
        tailPos[1]+=np.sign(tailHeadDistance[1])
        if(abs(tailHeadDistance[0]) > 0):
            tailPos[0]+=np.sign(tailHeadDistance[0])
    tailVisitedPosition.add((tailPos[0], tailPos[1]))

    # print(f"head: {headPos}, tail: {tailPos}, distance (before tail move): {tailHeadDistance}, distance (after tail move): {headPos-tailPos}")

print(f"tail visited {len(tailVisitedPosition)} positions")