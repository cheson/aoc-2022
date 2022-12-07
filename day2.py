# opp: A rock, B paper, C scissors
# me: X rock, Y paper, Z scissors
# 1 rock, 2 paper, 3 scissors
# 0 lost, 3 draw, 6 won

basePoints = {"X": 1, "Y": 2, "Z": 3}
winningCombos = ["AY", "BZ", "CX"]
tyingCombos = ["AX", "BY", "CZ"]

with open('./input/day_2.txt') as f:
	line = f.readline()
	scores = []
	while line:
		opp, me = line.split()
		key = opp + me
		points = basePoints[me]
		if key in winningCombos:
			points += 6
		if key in tyingCombos:
			points += 3
		scores.append(points)
		line = f.readline()
	print(sum(scores))

# x need to lose
# y need to draw
# z need to win

moveToLose = {"A": "S", "B": "R", "C": "P"}
moveToDraw = {"A": "R", "B": "P", "C": "S"}
moveToWin = {"A": "P", "B": "S", "C": "R"}
resultPoints = {"X": 0, "Y": 3, "Z": 6}
playPoints = {"R": 1, "P": 2, "S": 3}

with open('./input/day_2.txt') as f:
	line = f.readline()
	scores = []
	while line:
		opp, expectedResult = line.split()
		points = resultPoints[expectedResult]
		move = ""
		if expectedResult == "X":
			move = moveToLose[opp]
		if expectedResult == "Y":
			move = moveToDraw[opp]
		if expectedResult == "Z":
			move = moveToWin[opp]
		points += playPoints[move]
		scores.append(points)
		line = f.readline()
	print("PT 2", sum(scores))