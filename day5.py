# Load input file
f = open('day5_input.txt', 'r')
boardingCodes = f.read().split()
#boardingCodes = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

# Set vars
highestSeatId = 0
seats = []

# func
def splitter(rangeArray, lowUp = 'up'):
	if lowUp == 'low':
		rangeArray[1] = rangeArray[1] / 2
	else:
		rangeArray[0] = rangeArray[0] + rangeArray[1] / 2
		rangeArray[1] = rangeArray[1] / 2

	return rangeArray

# Loop trough boardingcodes
for boardingCode in boardingCodes:

	row = [0,128]
	column = [0,8]

	for char in boardingCode:
		if char == 'F':
			row = splitter(row, 'low')
		if char == 'B':
			row = splitter(row)
		if char == 'L':
			column = splitter(column, 'low')
		if char == 'R':
			column = splitter(column)

	seatId = row[0] * 8 + column[0]
	if seatId > highestSeatId:
		highestSeatId = seatId

	seats.append(seatId)

print(f'Part 1: {highestSeatId}')

# Part 2
fullSeats = list(range(int(highestSeatId)+1))

for seat in seats:
	fullSeats.remove(int(seat))

print(f'Part 2: {fullSeats}')

f.close()