import sys
import numpy as np

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

def loadMap(filename):
    with open(filename) as file:
        map = []
        for line in file.readlines():
            map.append([ord(letter) - ord('a') for letter in line.strip()])
    return np.array(map)

def possibleMoves(map, position):
    possibilities = []
    currentElevation = map[position]
    
    for position in [(position[0]-1, position[1]), (position[0]+1, position[1]), (position[0], position[1]-1), (position[0], position[1]+1)]:
        if position >=  (0, 0) and position[0] < map.shape[0] and position[1] < map.shape[1]:
            newElevation = map[position]
            if (newElevation - currentElevation <= 1):
                possibilities.append(position)

    return possibilities

def possibleAdditionalMoves(map, movelist, visited):
    lastMove = movelist[-1]
    newMoveLists = []
    for newMove in possibleMoves(map, lastMove):
        if newMove not in visited:
            currentNewMoveList = movelist[:]
            currentNewMoveList.append(newMove)
            visited.append(newMove)
            newMoveLists.append(currentNewMoveList)
    return (newMoveLists)

def searchUntilEnd(map, startingPosition, endPosition):
    visited = []
    allMoveLists = possibleAdditionalMoves(map, [startingPosition], visited)
    foundEnd = False
    while not foundEnd:
        newMoveListList = []
        for moveList in allMoveLists:
            if endPosition in moveList:
                return moveList
            newMoveListList.extend(possibleAdditionalMoves(map, moveList, visited))
        allMoveLists = newMoveListList
        print(f"currently {len(allMoveLists[0])} steps, with {len(allMoveLists)} different paths")
    


map = loadMap(getFileName())
print(map)
startingPosition = tuple(np.argwhere(map == -14)[0])
endPosition = tuple(np.argwhere(map == -28)[0])
print(startingPosition)
print(endPosition)
map[startingPosition] = 0
map[endPosition] = 25
print(map)
finalMoveList = searchUntilEnd(map, startingPosition, endPosition)
print(f"Reached goal in {len(finalMoveList)-1} steps")