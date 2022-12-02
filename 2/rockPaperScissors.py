import sys

class Match:
    winScoreDict = {
        ('A', 'A'): 3,
        ('A', 'B'): 6,
        ('A', 'C'): 0,
        ('B', 'A'): 0,
        ('B', 'B'): 3,
        ('B', 'C'): 6,
        ('C', 'A'): 6,
        ('C', 'B'): 0,
        ('C', 'C'): 3
    }

    choiceScoreDict = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    ownChoiceDict = {
        ('A', 'X'): 'C',
        ('A', 'Y'): 'A',
        ('A', 'Z'): 'B',
        ('B', 'X'): 'A',
        ('B', 'Y'): 'B',
        ('B', 'Z'): 'C',
        ('C', 'X'): 'B',
        ('C', 'Y'): 'C',
        ('C', 'Z'): 'A',
    }

    def __init__(self, opponent, outcome) -> None:
        self.opponent = opponent
        self.me = self.ownChoiceDict[opponent, outcome]

    def __str__(self) -> str:
        return f"{self.opponent}, {self.me}, Score: {self.getTotalScore()}"

    def getTotalScore(self):
        return self.winScoreDict[(self.opponent, self.me)] + self.choiceScoreDict[self.me]

def loadMatchHistory(filename):
    matchHistory = []
    with open(filename) as file:
        for line in file.readlines():
            matchHistory.append(Match(line[0], line[2]))

    return matchHistory

def getFileName():
    if (len(sys.argv) < 2):
        filename = 'input'
    else:
        filename = sys.argv[1]
    return filename

matchHistory = loadMatchHistory(getFileName())
matchHistoryScores = [match.getTotalScore() for match in matchHistory]

print(sum(matchHistoryScores))