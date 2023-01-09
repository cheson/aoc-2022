import threading
import logging

# part 1
TARGET = 2000000

# part 2
MIN_COORD = 0
MAX_COORD = 4000000

def tuningFreq(x, y):
	return x * 4000000 + y

def manhattanDistance(coordA, coordB):
	return abs(coordA[0] - coordB[0]) + abs(coordA[1] - coordB[1])

def coverage(center, manhattanDistance):
	global locationsCovered
	yDistToTarget = abs(center[1] - TARGET)
	# possible for this beacon to reach target row
	if yDistToTarget <= manhattanDistance:
		# remaining horizontal traverse after using yDistToTarget
		for x in range(0, manhattanDistance - yDistToTarget + 1):
			with lock:
				if center[1] >= TARGET:
					locationsCovered.add((center[0] - x, center[1] - yDistToTarget))
					locationsCovered.add((center[0] + x, center[1] - yDistToTarget))
				else:
					locationsCovered.add((center[0] - x, center[1] + yDistToTarget))
					locationsCovered.add((center[0] + x, center[1] + yDistToTarget))
						

sensorToDistanceCovered = dict()
locationsCovered = set()
beaconLocations = set()
lock = threading.Lock()

with open('./input/day_15.txt') as f:
	line = f.readline()
	while line:
		line = line[line.find('=') + 1:]
		sensorX = int(line[:line.find(',')])
		line = line[line.find('=') + 1:]
		sensorY = int(line[:line.find(':')])
		line = line[line.find('=') + 1:]
		beaconX = int(line[:line.find(',')])
		line = line[line.find('=') + 1:]
		beaconY = int(line)
		
		sensor = (sensorX, sensorY)
		beacon = (beaconX, beaconY)
		sensorToDistanceCovered[sensor] = manhattanDistance(sensor, beacon)
		beaconLocations.add(beacon)
		line = f.readline()

# part one
threads = list()
index = 0
for sensor in sensorToDistanceCovered:
    print("start thread:", index)
    x = threading.Thread(target=coverage, args=(sensor, sensorToDistanceCovered[sensor]))
    threads.append(x)
    x.start()
    index += 1

for index, thread in enumerate(threads):
    print("joining thread:", index)
    thread.join()
    print("thread done:", index)

# need to subtract out existing beacon locations bc technically it is possible for a beacon to be there
filtered = set(sorted([loc for loc in locationsCovered if loc[1] == TARGET])) - beaconLocations
print("result:", len(filtered))

# part two

def isCovered(coord):
	for sensor in sensorToDistanceCovered:
		sensorRange = sensorToDistanceCovered[sensor]
		distToSensor = manhattanDistance(coord, sensor)
		if distToSensor <= sensorRange:
			return True
	return False

# for each beacon, search its border + 1 to check isCovered
def getBorderLocations():
	borderLocations = set()
	for sensor in sensorToDistanceCovered:
		sensorRange = sensorToDistanceCovered[sensor]
		print("sensor", sensor, "range", sensorRange)

		sensorX = sensor[0]
		sensorY = sensor[1]

		'''
		eg, sensor range == 1
		from sensor, should look like below where we want Bs

				  B
				B X B
			  B	X S X B
				B X B
		          B
		'''
		potentialLocs = []
		for i in range(sensorRange + 1):
			xDiff = i
			yDiff = sensorRange - i

			# upper right quadrant
			potentialLocs.append((sensorX + xDiff, sensorY + yDiff + 1))
			# upper left quadrant
			potentialLocs.append((sensorX - xDiff - 1, sensorY + yDiff))
			# lower right quadrant
			potentialLocs.append((sensorX + xDiff + 1, sensorY - yDiff))
			# lower left quadrant
			potentialLocs.append((sensorX - xDiff, sensorY - yDiff - 1))


		for loc in potentialLocs:
			if loc[0] >= MIN_COORD and loc[0] <= MAX_COORD and loc[1] >= MIN_COORD and loc[1] <= MAX_COORD:
				borderLocations.add(loc)
        # + 2 gives unnecessary overlap, but it should work when added to set anyways
		# for i in range(sensorRange + 2):
		# 	xDiff = i
		# 	yDiff = sensorRange - i

		# 	# upper right quadrant
		# 	borderLocations.add((sensorX + xDiff, sensorY + yDiff + 1))
		# 	# upper left quadrant
		# 	borderLocations.add((sensorX - xDiff, sensorY + yDiff + 1))
		# 	# lower right quadrant
		# 	borderLocations.add((sensorX + xDiff, sensorY - yDiff - 1))
		# 	# lower left quadrant
		# 	borderLocations.add((sensorX - xDiff, sensorY - yDiff - 1))
	return borderLocations

def findDistressBeacon():
	borderLocations = getBorderLocations()
	print("len border locs", len(borderLocations))
	for loc in borderLocations:
		coveredDist = isCovered(loc)
		if coveredDist is False:
			print(tuningFreq(loc[0], loc[1]))
			return

findDistressBeacon()


