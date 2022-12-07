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
		priority = ord(foundItem) + 1
		if foundItem.isupper():
			priority -= ord('A')
			priority += 26
		else:
			priority -= ord('a')
		priorities.append(priority)
		line = f.readline()
	print(sum(priorities))
