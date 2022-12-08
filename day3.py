def calculatePriority(c):
	priority = ord(c) + 1
	if c.isupper():
		priority -= ord('A')
		priority += 26
	else:
		priority -= ord('a')
	return priority

with open('./input/day_3.txt') as f:
	line = f.readline()
	priorities = []
	while line:
		numItems = len(line) - 1 # accounting for /n
		midpoint = numItems // 2
		bagOne = line[:midpoint]
		bagTwo = line[midpoint:]
		foundItem = None
		for item in bagOne:
			if item in bagTwo:
				foundItem = item
		priorities.append(calculatePriority(foundItem))
		line = f.readline()
	print(sum(priorities))

def parseLine(line):
	parsedLine = [c for c in line]
	return parsedLine[:-1] # remove /n

# part two
with open('./input/day_3.txt') as f:
	lineOne = parseLine(f.readline())
	lineTwo = set(parseLine(f.readline()))
	lineThree = set(parseLine(f.readline()))

	priorities = []
	while lineOne:
		for c in lineOne:
			if c in lineTwo and c in lineThree:
				priorities.append(calculatePriority(c))
				break
		lineOne = parseLine(f.readline())
		lineTwo = set(parseLine(f.readline()))
		lineThree = set(parseLine(f.readline()))
	print(sum(priorities))



