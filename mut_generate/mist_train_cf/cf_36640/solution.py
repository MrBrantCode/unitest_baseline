"""
QUESTION:
You are given a string of passport data where each passport is a sequence of key-value pairs separated by spaces or newlines, and passports are separated by blank lines. Write a function `count_valid_passports(passport_data: str) -> int` that takes the passport data as input and returns the count of valid passports. A passport is valid if it contains the required fields ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid') and meets the following constraints: 
- byr: between 1920 and 2002
- iyr: between 2010 and 2020
- eyr: between 2020 and 2030
- hgt: a number followed by either "cm" (150-193) or "in" (59-76)
- hcl: a valid hexadecimal color code (# followed by exactly six characters 0-9 or a-f)
- ecl: one of "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
- pid: a nine-digit number, including leading zeroes
"""

def count_valid_passports(passport_data: str) -> int:
    passports = passport_data.strip().split('\n\n')
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_count = 0

    for passport in passports:
        fields = passport.replace('\n', ' ').split()
        field_dict = dict(field.split(':') for field in fields)
        if required_fields.issubset(field_dict.keys()):
            if 1920 <= int(field_dict['byr']) <= 2002 and \
               2010 <= int(field_dict['iyr']) <= 2020 and \
               2020 <= int(field_dict['eyr']) <= 2030 and \
               ((field_dict['hgt'].endswith('cm') and 150 <= int(field_dict['hgt'][:-2]) <= 193) or \
                (field_dict['hgt'].endswith('in') and 59 <= int(field_dict['hgt'][:-2]) <= 76)) and \
               field_dict['hcl'][0] == '#' and all(c in '0123456789abcdef' for c in field_dict['hcl'][1:]) and \
               field_dict['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} and \
               len(field_dict['pid']) == 9 and field_dict['pid'].isdigit():
                valid_count += 1

    return valid_count