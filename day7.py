# $ cd /
# $ ls
# 150961 cmnwnpwb
# 28669 hhcp.jzd
# dir jssbn
# dir lfrctthp
# 133395 lfrctthp.tlv
# dir ltwmz
# dir nmzntmcf
# dir vhj
# 256180 wbs.vmh
# 257693 zsntdzf
# $ cd jssbn
# $ ls
# 89372 dvlb
# dir lfrctthp
# dir pjzpjjq
import json

# list of current directory: [/, jssbn]

# map of 

# build n-tree

class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.files = {}
    self.size = 0
    self.subdirectories = []
    self.parent = parent

root = Directory("/")
currPath = [root] # actually seems extraneous
currDirectory = root

with open('./input/day_7.txt') as f:
	line = f.readline() # pass over cd /
	line = f.readline()
	while line:
		tokens = line.split()
		isCommand = tokens[0] == '$'
		if isCommand:
			if tokens[1] == 'cd':
				if tokens[2] == "..":
					currPath.pop()
					currDirectory = currDirectory.parent
				else:
					currPath.append(tokens[2])
					currDirectory = next(d for d in currDirectory.subdirectories if d.name == tokens[2])
			# no op for $ ls
		else:
			if tokens[0] == "dir":
				currDirectory.subdirectories.append(Directory(tokens[1], parent=currDirectory))
			else:
				currDirectory.files[tokens[1]] = int(tokens[0])
				currDirectory.size += int(tokens[0])

		line = f.readline()

	# traverse the tree and take any directories under limit
	# DIR_SIZE_LIMIT = 100000
	# resultSum = 0
	# directoriesToVisit = [root]
	# while len(directoriesToVisit) > 0:
	# 	currDirectory = directoriesToVisit.pop(0)
	# 	print("currDirectory", currDirectory.name)
	# 	directoriesToVisit += currDirectory.subdirectories
	# 	if currDirectory.size <= DIR_SIZE_LIMIT:
	# 		print("ADDING ", currDirectory.name, " WITH ", currDirectory.size)
	# 		resultSum += currDirectory.size
	# print(resultSum)

resultSum = [0]
directoriesBiggerThanNeeded = []
def traverseTree(currDirectory, level, resultSum, resultDirs):
	if currDirectory is None:
		return 0
	# print("-" * level, currDirectory.name + " " + json.dumps(currDirectory.files))
	currDirectorySize = currDirectory.size
	for d in currDirectory.subdirectories:
		currDirectorySize += traverseTree(d, level + 1, resultSum, resultDirs)
	if currDirectorySize <= 100000:
		resultSum[0] += currDirectorySize
	if currDirectorySize >= 913445:
		resultDirs.append(currDirectorySize)
	print(currDirectory.name, currDirectorySize)
	return currDirectorySize
traverseTree(root, 0, resultSum, directoriesBiggerThanNeeded)
print(resultSum)




print(70000000 - 40913445)
print(30000000 - 29086555)

print(sorted(directoriesBiggerThanNeeded))
# needs 913445


