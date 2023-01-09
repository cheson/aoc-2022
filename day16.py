currValve = "AA"
timeRemaining = 30
currFlowRate = 0
totalPressureRelease = 0

valveFlowRates = dict() # AA => 0, BB => 13, ...
connectedValves = dict() # AA -> [DD, II, BB], ...

with open('./input/day_16.txt') as f:
	line = f.readline()
	while line:
		line = f.readline()

# recursively explore each option?
# 	keep track of valves opened
# 	when either time remaining expires or no more valves unexplored, return
# 	