O_ROCK = "A"
O_PAPER = "B"
O_SCISSORS = "C"

P_ROCK = "A"
P_PAPER = "B"
P_SCISSORS = "C"

LOOSE = "X"
DRAW = "Y"
WIN = "Z"

with open("./02/input.txt", "r") as f:
    rounds = [ln.split(" ") for ln in f.read().split("\n") if ln]


def chooseAction(round: [int, int]):
    actions = {
        O_ROCK: [P_SCISSORS, P_ROCK, P_PAPER],
        O_SCISSORS: [P_PAPER, P_SCISSORS, P_ROCK],
        O_PAPER: [P_ROCK, P_PAPER, P_SCISSORS],
    }

    enemyMove = round[0]
    outcome = round[1]
    if outcome == WIN:
        return [1, actions[enemyMove][2]]
    elif outcome == DRAW:
        return [0, actions[enemyMove][1]]
    elif outcome == LOOSE:
        return [-1, actions[enemyMove][0]]


def getScore(win: bool, played: str):
    score = 0
    if win == 0:
        score += 3
    elif win == 1:
        score += 6

    score += {P_ROCK: 1, P_PAPER: 2, P_SCISSORS: 3}[played]

    return score


sum = 0
for round in rounds:
    action = chooseAction(round)

    score = getScore(action[0], action[1])

    # print(round, action)

    sum += score

print("=>", sum)
