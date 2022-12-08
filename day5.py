#     [H]         [H]         [V]    
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9 

def readStacks(f):
	line = f.readline()
	stacks = [["G", "P", "N", "R"],
	["H", "V", "S", "C", "L", "B", "J", "T"],
	["L", "N", "M", "B", "D", "T"],
	["B", "S", "P", "V", "R"],
	["H", "V", "M", "W", "S", "Q", "C", "G"],
	["J", "B", "D", "C", "S", "Q", "W"],
	["L", "Q", "F"],
	["V", "F", "L", "D", "T", "H", "M", "W"],
	["F", "J", "M", "V", "B", "P", "L"]] 
	while line != '\n':
		line = f.readline()
	return stacks

def parseInstruction(line):
	# move 4 from 1 to 9
	tokens = line.split()
	return [int(x) for x in tokens if x.isnumeric()]

with open('./input/day_5.txt') as f:
	stacks = readStacks(f)
	line = f.readline()
	while line:
		# move 4 from 1 to 9
		moveNum, source, dest = parseInstruction(line)
		# account for zero indexing
		source -= 1
		dest -= 1
		print(moveNum, source, dest)

		for i in range(moveNum):
			temp = stacks[source].pop(0)
			stacks[dest].insert(0, temp)

		line = f.readline()
	print([stack[0] for stack in stacks])


# part two
with open('./input/day_5.txt') as f:
	stacks = readStacks(f)
	line = f.readline()
	while line:
		# move 4 from 1 to 9
		moveNum, source, dest = parseInstruction(line)
		# account for zero indexing
		source -= 1
		dest -= 1
		print(moveNum, source, dest)

		stacks[dest] = stacks[source][:moveNum] + stacks[dest]
		stacks[source] = stacks[source][moveNum:]

		line = f.readline()
	print([stack[0] for stack in stacks])