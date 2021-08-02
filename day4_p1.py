# Load input file
f = open('day4_input.txt', 'r')
passportList = f.read().split('\n\n')

# Set
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
numValid = 0

# Loop trough passports
for passport in passportList:
    passFields = passport.split()
    valid = True

    for reqField in requiredFields:
        present = False

        for passField in passFields:
            if reqField == passField[0:3]:
                present = True
                break

        if not present:
            valid = False
            break

    if valid:
        numValid += 1

print(f'Part 1: {numValid}')

f.close()