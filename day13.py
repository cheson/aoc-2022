import functools
import json

correctPairIndices = []

def packetsOrdered(packetOne, packetTwo):
	oneIsList = type(packetOne) == list
	twoIsList = type(packetTwo) == list

	# one or both inputs are lists
	if oneIsList or twoIsList:
		if not oneIsList:
			packetOne = [packetOne]
		if not twoIsList:
			packetTwo = [packetTwo]
		for i, valOne in enumerate(packetOne):
			if i >= len(packetTwo):
				return 1
			valTwo = packetTwo[i]
			res = packetsOrdered(valOne, valTwo)
			if res != 0:
				return res
		if len(packetOne) == len(packetTwo):
			return 0
		return -1
	# both inputs are numbers
	else:
		ret = 0
		if packetOne < packetTwo:
			ret = -1
		elif packetOne > packetTwo:
			ret = 1
		return ret
	
with open('./input/day_13.txt') as f:
	index = 1
	packetOne = f.readline().strip('\n')
	packetTwo = f.readline().strip('\n')
	f.readline() # newline

	while len(packetOne) > 0 and len(packetTwo) > 0:
		if packetsOrdered(json.loads(packetOne), json.loads(packetTwo)) == -1:
			correctPairIndices.append(index)
		index += 1

		packetOne = f.readline().strip('\n')
		packetTwo = f.readline().strip('\n')
		f.readline() # newline

print("RESULT", functools.reduce(lambda a, b: a+b, correctPairIndices, 0))
print(len(correctPairIndices))
print(correctPairIndices)

# part two
packets = [[[2]], [[6]]]
with open('./input/day_13.txt') as f:
	packetOne = f.readline().strip('\n')
	packetTwo = f.readline().strip('\n')
	f.readline() # newline

	while len(packetOne) > 0 and len(packetTwo) > 0:
		packets.append(json.loads(packetOne))
		packets.append(json.loads(packetTwo))

		packetOne = f.readline().strip('\n')
		packetTwo = f.readline().strip('\n')
		f.readline() # newline

print(len(packets))
packets = sorted(packets, key=functools.cmp_to_key(packetsOrdered))
indexA = packets.index([[2]]) + 1
indexB = packets.index([[6]]) + 1
print(indexA * indexB)