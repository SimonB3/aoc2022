import sys

def loadSectionAssignmentSetPairs(filename):
    allRangePairs = []
    with open(filename) as file:
        for line in file.readlines():
            sections_starts_and_stops = [[int(rawval) for rawval in section.split('-')] for section in line.strip().split(',')]
            allRangePairs.append([set(range(innerlist[0], innerlist[1]+1)) for innerlist in sections_starts_and_stops])            

    return allRangePairs

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

allSectionPairs = loadSectionAssignmentSetPairs(getFileName())
#print(allSectionPairs)
isSectionContained = [sections[0].issubset(sections[1]) or sections[1].issubset(sections[0]) for sections in allSectionPairs]
#print(isSectionContained)
print(f"Complete overlap: {sum(isSectionContained)}")
isOverlap = [not sections[0].isdisjoint(sections[1]) for sections in allSectionPairs]
print(f"Any overlap: {sum(isOverlap)}")