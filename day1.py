# read in input
# while not empty line, keep reading and accumulating calories
# with each empty line, add elfs calorie count to a table

with open('./input/day_1.txt') as f:
	line = f.readline()
	currMaxElf = 0
	currCalories = 0
	elfCalories = []
	while line:
		if line == '\n':
			elfCalories.append(currCalories)
			if currCalories > elfCalories[currMaxElf]:
				currMaxElf = len(elfCalories) - 1
			currCalories = 0
		else:
			currCalories += int(line)
		line = f.readline()
	print("max elf", currMaxElf)
	print("max calories", elfCalories[currMaxElf])

	# part 2
	elfCalories = sorted(elfCalories, reverse=True)
	print(sum(elfCalories[:3]))