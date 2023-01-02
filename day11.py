class Monkey:
  def __init__(self, number, items, test, trueDest, falseDest):
  	self.number = number
  	self.items = items
  	self.test = test
  	self.trueDest = trueDest
  	self.falseDest = falseDest
  	self.itemsInspected = 0

def parseMonkey():
	# number
	line = f.readline()
	if len(line) == 0:
		return None
	monkeyNumber = int(line.split()[1].replace(":", ""))

	# starting items
	line = f.readline()
	startingItems = [int(s) for s in line[line.index(":") + 1:].strip().split(",")]
	
	# operation -> hardcode
	line = f.readline()

	# test
	line = f.readline()
	test = int(line[line.index("by") + 3:])
	
	# true dest
	line = f.readline()
	trueDest = int(line[line.index("monkey") + 7:])

	# false dest
	line = f.readline()
	falseDest = int(line[line.index("monkey") + 7:])

	line = f.readline()
	return Monkey(monkeyNumber, startingItems, test, trueDest, falseDest)

monkeys = dict()
with open('./input/day_11.txt') as f:
	newMonkey = parseMonkey()
	while newMonkey is not None:
		monkeys[newMonkey.number] = newMonkey
		newMonkey = parseMonkey()

for roundNum in range(10000):
	print("ROUND", roundNum)
	for monkeyNum in range(len(monkeys)):
		# print("MONKEY", monkeyNum)
		monkey = monkeys[monkeyNum]
		while len(monkey.items) > 0:
			item = monkey.items.pop(0)
			# print("ITEM", item)
			monkey.itemsInspected += 1

			# inspection
			if monkeyNum == 0:
				item *= 17
			elif monkeyNum == 1:
				item *= 11
			elif monkeyNum == 2:
				item += 4
			elif monkeyNum == 3:
				item *= item
			elif monkeyNum == 4:
				item += 7
			elif monkeyNum == 5:
				item += 8
			elif monkeyNum == 6:
				item += 5
			elif monkeyNum == 7:
				item += 3

			item = item % 9699690
			# post inspection worry reduction
			# part 2
			# item = item // 3

			# test
			testDest = item % monkey.test == 0

			# throw
			finalDest = None
			if testDest:
				finalDest = monkey.trueDest
			else:
				finalDest = monkey.falseDest
			monkeys[finalDest].items.append(item)

for monkeyNum in range(len(monkeys)):
	monkey = monkeys[monkeyNum]
	print(monkeyNum, monkey.itemsInspected)

