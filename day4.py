def parseLine(line):
	resultPairs = []
	pairOne, pairTwo = line.strip().split(",")
	for pair in [pairOne, pairTwo]:
		resultPairs.append([int(x) for x in pair.split("-")])
	return resultPairs

with open('./input/day_4.txt') as f:
	line = f.readline()
	count = 0
	while line:
		resultPairs = parseLine(line)

		# sort pairs by lowest low, then highest high
		# grab first pair
		sortedPairs = sorted(resultPairs, key=lambda x: (x[0], -x[1]))

		maxRange = sortedPairs[0]

		for pair in sortedPairs[1:]:
			if pair[0] >= maxRange[0] and pair[1] <= maxRange[1]:
				count += 1

		line = f.readline()
	print(count)

# part two 
with open('./input/day_4.txt') as f:
	line = f.readline()
	count = 0
	while line:
		resultPairs = parseLine(line)

		# sort pairs by lowest low, then highest high
		# grab first pair
		sortedPairs = sorted(resultPairs, key=lambda x: (x[0], -x[1]))

		maxRange = sortedPairs[0]

		for pair in sortedPairs[1:]:
			if (pair[0] in range(maxRange[0], maxRange[1] + 1)) or (pair[1] in range(maxRange[0], maxRange[1] + 1)):
				count += 1

		line = f.readline()
	print(count)
