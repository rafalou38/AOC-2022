with open("./input.txt", "r") as f:
	rounds = [ln.split(" ") for ln in f.read().split("\n") if ln]


def win(round: [int, int]):
	"""
	-1 : loose
	 0 : draw
	 1 : win
	"""
	if (round[0] == "A"):
		if round[1] == "Z": return -1
		elif round[1] == "Y": return 1
	elif (round[0] == "B"):
		if round[1] == "X": return -1
		elif round[1] == "Z": return 1
	elif (round[0] == "C"):
		if round[1] == "Y": return -1
		elif round[1] == "X": return 1

	return 0


def getScore(win: bool, played: str):
	score = 0
	if (win == 0): score += 3
	elif (win == 1): score += 6

	score += {"X": 1, "Y": 2, "Z": 3}[played]

	return score


sum = 0
for round in rounds:
	result = win(round)
	score = getScore(result, round[1])

	print(round, result, score)

	sum += score

print("=>", sum)
