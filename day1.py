f = open('day1_input.txt', 'r')
inputCodes = f.read().split()
inputCodes = list(map(int, inputCodes))

# Part 1
for i in inputCodes:
    for j in inputCodes:
        if i + j == 2020:
           print(f"Part 2 answer: {i} + {j} = 2020 (* = {i*j})")

# Part 2
for i in inputCodes:
    for j in inputCodes:
        for k in inputCodes:
            if i + j + k == 2020:
                print(f"Part 2: {i} + {j} + {k} = 2020 (* = {i*j*k})")

f.close()