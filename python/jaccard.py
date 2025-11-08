import sys

def read_file(filename):
	names = []
	with open(filename) as fp:
		for line in fp:
			names.append(line.rstrip())
	return names

names1 = read_file(sys.argv[1])
names2 = read_file(sys.argv[2])

unique1 = []
unique2 = []
shared = []
for name in names1:
	if name in names2: shared.append(name)
	else: unique1.append(name)

for name in names2:
	if name not in names1: unique2.append(name)

print(unique1)
print(unique2)
print(shared)
print(len(shared) / ( len(unique1) + len(unique2) + len(shared) ))
