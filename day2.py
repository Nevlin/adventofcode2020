# Load input file
f = open('day2_input.txt', 'r')
inputStrings = f.read().split('\n')[:-1]

# Set vars
numPasscodes = len(inputStrings)
numCodesPartTwo = 0

# Loop trough passwords
for passString in inputStrings:
    passList = passString.split(" ")
    passRangeTemp = passList[0].split("-")
    passRange = [int(i) for i in passRangeTemp]
    passChar = passList[1][:1]
    passCode = passList[2]

    numChar = 0
    for char in passCode:
        if char == passChar:
            numChar += 1

    if numChar < passRange[0] or numChar > passRange[1]:
        numPasscodes -= 1

    # Part Two
    posOneChar = passCode[passRange[0]-1]
    posTwoChar = passCode[passRange[1]-1]

    if posOneChar == passChar and posTwoChar != passChar or posOneChar != passChar and posTwoChar == passChar:
        numCodesPartTwo += 1

print(f'Part 1: {numPasscodes}')
print(f'Part 2: {numCodesPartTwo}')

f.close()