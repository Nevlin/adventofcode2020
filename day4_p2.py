import re

# Load input file
f = open('day4_input.txt', 'r')
passportList = f.read().split('\n\n')

# Set
requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
numValid = 0

# Checks funcs
def checkValid(field, fieldValue):
    validCheck = False

    if field == 'byr':
        if len(fieldValue) == 4 and 1920 <= int(fieldValue) <= 2002:
            validCheck = True

    elif field == 'iyr':
        if len(fieldValue) == 4 and 2010 <= int(fieldValue) <= 2020:
            validCheck = True

    elif field == 'eyr':
        if len(fieldValue) == 4 and 2020 <= int(fieldValue) <= 2030:
            validCheck = True

    elif field == 'hgt':
        if fieldValue[-2:] == 'cm':
            if 150 <= int(fieldValue[:-2]) <= 193:
                validCheck = True
        if fieldValue[-2:] == 'in':
            if 59 <= int(fieldValue[:-2]) <= 76:
                validCheck = True

    elif field == 'hcl':
        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', fieldValue):
            validCheck = True

    elif field == 'ecl':
        for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            if color == fieldValue:
                validCheck = True
                break

    elif field =='pid':
        if len(fieldValue) == 9:
            validCheck = True
    
    return validCheck

# Loop trough passports
for passport in passportList:
    passFields = passport.split()
    valid = True

    for reqField in requiredFields:
        presentAndValid = False

        for passField in passFields:
            if reqField == passField[0:3]:
    
                # valid check
                if checkValid(reqField, passField.split(':')[1]):
                    presentAndValid = True
                    break

        if not presentAndValid:
            valid = False
            break

    if valid:
        numValid += 1

print(f'Part 2: {numValid}')

f.close()