import sys

class Match:
    choiceScoreDict = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    outcomeDict = {
        'X': 2,
        'Y': 0,
        'Z': 1
    }

    ownChoiceDict = {
        0: 'C',
        1: 'A',
        2: 'B',
    }

    def __init__(self, opponent, outcome) -> None:
        self.opponent = opponent
        self.me = self.getOwnChoice(opponent, outcome)

    def __str__(self) -> str:
        return f"{self.opponent}, {self.me}, Score: {self.calculateWinScore()} + {self.choiceScoreDict[self.me]} = {self.getTotalScore()}"

    def getOwnChoice(self, opponent, outcome):
        return self.ownChoiceDict[(self.choiceScoreDict[opponent] + self.outcomeDict[outcome]) % 3]

    def calculateWinScore(self):
        return ((((self.choiceScoreDict[self.opponent] - self.choiceScoreDict[self.me]) *-1) + 4) % 3) * 3

    def getTotalScore(self):
        return self.calculateWinScore() + self.choiceScoreDict[self.me]

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

# [print(match) for match in matchHistory]
# print(matchHistoryScores)
print(sum(matchHistoryScores))