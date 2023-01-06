sandSource = (500, 0)
# could iterate once to find max and min X/Y or resize dynamically, but just
# hardcoding this
rockGrid = [["."] * 1000 for i in range(1000)]

# part 2
# used map for dynamic sizing, should've done that instead of grid for pt1
rockMap = dict()

maxY = 0

with open('./input/day_14.txt') as f:
	line = f.readline()

	while line:
		paths = line.strip().replace(" ", "").split("->")
		paths = [[int(c) for c in coord.split(",")] for coord in paths]
		for i in range(1, len(paths)):
			prev = paths[i-1]
			curr = paths[i]
			currX = curr[0]
			currY = curr[1]
			prevX = prev[0]
			prevY = prev[1]

			maxY = max(max(maxY, currY), prevY)

			xDiff = currX - prevX
			yDiff = currY - prevY

			if xDiff == 0:
				for y in range(min(prevY, currY), max(prevY, currY) + 1):
					rockGrid[y][currX] = "#"
					rockMap[(currX, y)] = '#'
			if yDiff == 0:
				for x in range(min(prevX, currX), max(prevX, currX) + 1):
					rockGrid[currY][x] = "#"
					rockMap[(x, currY)] = '#'
		line = f.readline()

def simulateSand(rockGrid, sandSource):
	movements = [(0, 1), (-1, 1), (1, 1)]
	grainsOfSand = 0
	# simulate continuous flow of sand from source
	while True:
		sandMoving = True
		currSandPos = sandSource
		# simulate one grain of sand
		while sandMoving:
			sandMoving = False
			for movement in movements:
				tentativePos = [currSandPos[0] + movement[0], currSandPos[1] + movement[1]]
				# out of bounds
				if tentativePos[0] >= len(rockGrid[0]) or tentativePos[0] < 0 or tentativePos[1] >= 1000:
					print("GRAINS PT1: ", grainsOfSand)
					return
				if rockGrid[tentativePos[1]][tentativePos[0]] == ".":
					sandMoving = True
					currSandPos = tentativePos
					break
		rockGrid[currSandPos[1]][currSandPos[0]] = 'o'
		grainsOfSand += 1

def simulateSandPartTwo(rockGrid, sandSource, floorY):
	movements = [(0, 1), (-1, 1), (1, 1)]
	grainsOfSand = 0
	# simulate continuous flow of sand from source
	while True:
		sandMoving = True
		currSandPos = sandSource
		# simulate one grain of sand
		while sandMoving:
			sandMoving = False
			for movement in movements:
				tentativePos = (currSandPos[0] + movement[0], currSandPos[1] + movement[1])
				# can move in that direction
				if tentativePos not in rockMap and tentativePos[1] < floorY:
					sandMoving = True
					currSandPos = tentativePos
					break
		rockMap[currSandPos] = 'o'
		grainsOfSand += 1
		if currSandPos == (500, 0):
			print("GRAINS PT2: ", grainsOfSand)
			break

# part 1
simulateSand(rockGrid, sandSource)

# part 2
floorY = maxY + 2
simulateSandPartTwo(rockMap, sandSource, floorY)


