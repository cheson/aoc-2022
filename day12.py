
# using (row, col)
startPos = None
endPos = None
aPositions = []

class Position:
  def __init__(self, row, column, level):
  	self.coord = (row, column)
  	self.level = level

def parseGrid():
	global startPos, endPos, aPositions
	grid = []
	with open('./input/day_12.txt') as f:
		line = f.readline()
		currRow = 0
		while line:
			newRow = [] * len(line)
			for currCol, c in enumerate(line):
				if c == 'S':
					startPos = Position(currRow, currCol, 0)
					c = 'a'
				if c == 'E':
					endPos = Position(currRow, currCol, 0)
					c = 'z'
				if c != '\n':
					newRow.append(ord(c) - ord('a'))
				if c == 'a':
					aPositions.append(Position(currRow, currCol, 0))
			grid.append(newRow)
			line = f.readline()
			currRow += 1
	return grid

def search(grid, searchOptions, visited):
	while len(searchOptions) != 0:
		nextOption = searchOptions.pop(0)
		searchHead = nextOption.coord
		level = nextOption.level
		if searchHead not in visited:
			visited.add(searchHead)
			# FOUND
			if searchHead == endPos.coord:
				return level
			for rowDiff in range(-1, 2):
				for colDiff in range(-1, 2):
					# 0 is center, 1 is vertical and horizontal, and 2 is diagonal edges
					if abs(rowDiff + colDiff) == 1:
						row = searchHead[0]
						col = searchHead[1]
						nextRow = row + rowDiff
						nextCol = col + colDiff
						inBounds = nextRow >= 0 and nextRow < len(grid) and nextCol >= 0 and nextCol < len(grid[0])
						if (nextRow, nextCol) not in visited and inBounds:
								nextVal = grid[nextRow][nextCol]
								currVal = grid[row][col]
								if nextVal - currVal <= 1:
									searchOptions.append(Position(nextRow, nextCol, level + 1))
	# temp big num to help sort since None can't be compared to int
	return 100000

grid = parseGrid()

# part 1
searchOptions = [startPos]
visited = set()
print(search(grid, searchOptions, visited))

# part 2
results = []
for aPos in aPositions:
	visited = set()
	results.append(search(grid, [aPos], visited))
print(sorted(results))
