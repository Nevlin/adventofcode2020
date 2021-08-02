f = open('day3_input.txt', 'r')
treeRows = f.read().split()

rowLength = len(treeRows[0])
numTrees = 0
xPos = 0

for row in treeRows:
    if row[xPos] == '#':
        numTrees += 1

    # Add
    xPos += 3
    if xPos >= rowLength:
        xPos -= rowLength

print(f'Part 1: {numTrees}')

# Part 2

def calcTress( numRight, numDown ):

    numTrees = 0
    xPos = 0

    for i, row in enumerate(treeRows):

        # Check odd
        if numDown == 2 and i % 2:
            continue

        if row[xPos] == '#':
            numTrees += 1
        
        xPos += numRight
        if xPos >= rowLength:
            xPos -= rowLength

    return numTrees

answerTwo = calcTress(1,1) * calcTress(3,1) * calcTress(5,1) * calcTress(7,1) * calcTress(1,2)
print(f'Part 2: {answerTwo}')

f.close()