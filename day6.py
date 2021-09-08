# Load input file
f = open('day6_input.txt', 'r')
inputText = f.read()
answers = inputText.split('\n')

# Set vars
uniques = []
groupCount = 0
totalCount = 0

# Loop trough answers
for awnser in answers:
	if awnser == '':
		totalCount += groupCount
		uniques = []
		groupCount = 0
	else:
		for char in awnser:
			if not char in uniques:
				uniques.append(char)
				groupCount += 1

print(f'Part 1: {totalCount}')

# Part 2
# Set
totalCount = 0
groupAnswers = inputText.strip().split("\n\n")

# loop trough group answers
for group in groupAnswers:
	groupArray = group.split("\n")
	if len(groupArray) == 1:
		totalCount += len(groupArray[0])
	else:
		charCount = {}
		for awnser in groupArray:
			for char in awnser:
				if char not in charCount:
					charCount[char] = 1
				else:
					charCount[char] += 1
		for char, value in charCount.items():
			if value == len(groupArray):
				totalCount += 1

print(f'Part 2: {totalCount}')
