import sys

def loadElfsums(filename):
    elfsums = [0]
    with open(filename) as f:
        for line in f.readlines():
            if line.strip() == '':
                elfsums.append(0)
            else:
                elfsums[-1] += int(line.strip())
    return elfsums

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'indata_1'
    else:
        filename = sys.argv[1]
    return filename
    
sortedOnSum = sorted(loadElfsums(getFileName()), reverse=True)

print(f"Elf carrying the most carries {sortedOnSum[0]}.")
print(f"Top 3 elves carries in total: {sum(sortedOnSum[0:3])}.")