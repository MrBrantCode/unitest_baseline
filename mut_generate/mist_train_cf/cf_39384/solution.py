"""
QUESTION:
Implement the function `validate_passport_data(passport_data: dict) -> bool` that takes a dictionary `passport_data` containing key-value pairs representing different fields of passport data. The function should return True if the passport data is valid according to the following rules, and False otherwise.

The rules are as follows:
- 'byr' (Birth Year): Four digits; at least 1920 and at most 2002.
- 'iyr' (Issue Year): Four digits; at least 2010 and at most 2020.
- 'eyr' (Expiration Year): Four digits; at least 2020 and at most 2030.
- 'hgt' (Height): A number followed by either cm or in. If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
- 'hcl' (Hair Color): A '#' followed by exactly six characters 0-9 or a-f.
- 'ecl' (Eye Color): Exactly one of: amb blu brn gry grn hzl oth.
- 'pid' (Passport ID): A nine-digit number, including leading zeroes.
- 'cid' (Country ID) is ignored.
"""

import re

def validate_passport_data(passport_data: dict) -> bool:
    def validate_year(value, min_year, max_year):
        return value.isdigit() and min_year <= int(value) <= max_year

    def validate_height(value):
        if value.endswith('cm'):
            height = int(value[:-2])
            return 150 <= height <= 193
        elif value.endswith('in'):
            height = int(value[:-2])
            return 59 <= height <= 76
        return False

    def validate_hair_color(value):
        return re.match(r'^#[0-9a-f]{6}$', value) is not None

    def validate_eye_color(value):
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def validate_passport_id(value):
        return re.match(r'^\d{9}$', value) is not None

    validations = {
        'byr': lambda x: validate_year(x, 1920, 2002),
        'iyr': lambda x: validate_year(x, 2010, 2020),
        'eyr': lambda x: validate_year(x, 2020, 2030),
        'hgt': validate_height,
        'hcl': validate_hair_color,
        'ecl': validate_eye_color,
        'pid': validate_passport_id
    }

    for key, value in passport_data.items():
        if key in validations and not validations[key](value):
            return False

    return True