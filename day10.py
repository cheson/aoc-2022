inspect = [20, 60, 100, 140, 180, 220]
cycle = 1
reg = 1
total = 0
result = [['.'] * 40 for i in range(6)]
currRow = 0

def incrementCycle():
	global cycle, total, reg, result
	# print(reg)
	currPos = (cycle - 1) % 40
	currRow = (cycle - 1) // 40
	print(currPos)
	if (reg - 1) <= currPos and currPos <= reg + 1:
		result[currRow][currPos] = '#'
	if cycle in inspect:
		total += cycle * reg
	cycle = cycle + 1


with open('./input/day_10.txt') as f:
	line = f.readline()
	while line:
		inst = line.split()
		if len(inst) == 1:
			incrementCycle()
		else:
			incrementCycle()
			incrementCycle()
			reg += int(inst[1])
		line = f.readline()

print(total)
print(result)

for line in result:
	print(*line)
# [['#', '#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#', '.'],
#  ['#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.'],
#  ['#', '#', '#', '.', '.', '#', '#', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '#', '.', '.'],
#  ['#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
#  ['#', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
#  ['#', '#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '#', '.']]