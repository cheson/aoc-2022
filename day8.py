
treeGrid = []

with open('./input/day_8.txt') as f:
	line = f.readline()
	while line:
		treeHeights = [int(h) for h in line if h != '\n']
		treeGrid.append(treeHeights)
		line = f.readline()

numCols = len(treeGrid[0])
numRows = len(treeGrid)

# can't do [[0]*numCols]*numRows bc python will copy pointers to the row lists instead of creating distinct copies
results = [[0]*numCols for y in range(numRows)]

def visibleTrees(treeHeights):
	currHighest = -1
	visibleTrees = [0] * len(treeHeights)
	for i, h in enumerate(treeHeights):
		if h > currHighest:
			visibleTrees[i] = 1
			currHighest = h
	currHighest = -1
	for i in reversed(range(len(treeHeights))):
		h = treeHeights[i]
		if h > currHighest:
			visibleTrees[i] = 1
			currHighest = h
	return visibleTrees

for i, row in enumerate(treeGrid):
	row = visibleTrees(row)
	for j, isVisible in enumerate(row):
		results[i][j] = isVisible

for colNum in range(numCols):
	col = [row[colNum] for row in treeGrid]
	col = visibleTrees(col)
	for row in range(len(col)):
		results[row][colNum] = col[row] | results[row][colNum]

print(sum([sum(row) for row in results]))

# part 2
def scoreHelper(currTrees, treeHeight):
	score = 0
	for h in currTrees:
		score += 1
		if h >= treeHeight:
			break
	return score 

def calculateScore(x, y):
	row = treeGrid[y]
	col = [row[x] for row in treeGrid]
	treeHeight = treeGrid[y][x]
	# go up
	currTrees = col[:y]
	currTrees.reverse()
	score = scoreHelper(currTrees, treeHeight)
	# go right
	currTrees = row[x+1:]
	score = score * scoreHelper(currTrees, treeHeight)
	# go down
	currTrees = col[y+1:]
	score = score * scoreHelper(currTrees, treeHeight)
	# go left
	currTrees = row[:x]
	currTrees.reverse()
	score = score * scoreHelper(currTrees, treeHeight)

	return score


highestScore = 0
for col in range(numCols):
	for row in range(numRows):
		score = calculateScore(col, row)
		highestScore = max(score, highestScore)
print(highestScore)