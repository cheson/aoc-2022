def sign(a):
    return (a > 0) - (a < 0)

def adjustedTailLoc(headLoc, tailLoc):
	xDiff = headLoc[0] - tailLoc[0]
	yDiff = headLoc[1] - tailLoc[1]
	newTailLoc = list(tailLoc)

	if abs(xDiff) <= 1 and abs(yDiff) <= 1:
		return tuple(newTailLoc)

	if xDiff == 0 and yDiff > 1:
		newTailLoc[1] += 1
	if xDiff == 0 and yDiff < -1:
		newTailLoc[1] -= 1
	if yDiff == 0 and xDiff > 1:
		newTailLoc[0] += 1
	if yDiff == 0 and xDiff < -1:
		newTailLoc[0] -= 1

	if abs(xDiff) >= 1 and abs(yDiff) >= 1:
		newTailLoc[0] += sign(xDiff)
		newTailLoc[1] += sign(yDiff)

	return tuple(newTailLoc)


with open('./input/day_9.txt') as f:
	move = f.readline()
	# tuples are more memory efficient but not mutable
	start = (0, 0)
	tailLoc = start
	headLoc = [0, 0]
	visited = set([start])
	while move:
		direction, magnitude = move.split()
		magnitude = int(magnitude)

		for i in range(magnitude):
			if direction == "D":
				headLoc[1] -= 1
			elif direction == "U":
				headLoc[1] += 1
			elif direction == "L":
				headLoc[0] -= 1
			elif direction == "R":
				headLoc[0] += 1
			tailLoc = adjustedTailLoc(headLoc, tailLoc)
			visited.add(tailLoc)

		move = f.readline()

	print(len(visited))

# part 2
with open('./input/day_9.txt') as f:
	move = f.readline()
	# tuples are more memory efficient but not mutable
	locs = dict()
	for i in range(10):
		locs[i] = [0, 0]
	visited = set([(0, 0)])
	moveNum = 1
	while move:
		direction, magnitude = move.split()
		magnitude = int(magnitude)
		for i in range(magnitude):
			headLoc = locs[0]
			if direction == "D":
				headLoc[1] -= 1
			elif direction == "U":
				headLoc[1] += 1
			elif direction == "L":
				headLoc[0] -= 1
			elif direction == "R":
				headLoc[0] += 1
			for i in range(9):
				firstLoc = locs[i]
				secondLoc = locs[i+1]
				adjustedLoc = adjustedTailLoc(firstLoc, secondLoc)
				locs[i+1] = adjustedLoc
			visited.add(tuple(locs[9]))
		move = f.readline()
	print(len(visited))




