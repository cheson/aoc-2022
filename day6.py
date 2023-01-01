with open('./input/day_6.txt') as f:
	signal = f.readline()
	for i in range(len(signal) - 4):
		segment = signal[i:i+4]
		if len(segment) == len(set(segment)):
			print(i + 4)
			break

with open('./input/day_6.txt') as f:
	signal = f.readline()
	for i in range(len(signal) - 14):
		segment = signal[i:i+14]
		if len(segment) == len(set(segment)):
			print(i + 14)
			break
