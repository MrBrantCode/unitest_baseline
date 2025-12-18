"""
QUESTION:
You are given a list of passport data where each passport is a sequence of key-value pairs. Write a function called `count_valid_passports` that takes this list and returns the number of valid passports. A passport is valid if it contains all seven required fields (byr, iyr, eyr, hgt, hcl, ecl, pid), and the data within these fields are valid according to specific rules: 
- byr (Birth Year) - four digits; at least 1920 and at most 2002.
- iyr (Issue Year) - four digits; at least 2010 and at most 2020.
- eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
- hgt (Height) - a number followed by either cm or in: if cm, the number must be at least 150 and at most 193; if in, the number must be at least 59 and at most 76.
- hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
- ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
- pid (Passport ID) - a nine-digit number, including leading zeroes.
"""

import re

def count_valid_passports(passport_data):
    def is_valid(passport):
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        fields = dict(field.split(":") for field in passport.split())
        if required_fields.issubset(fields.keys()):
            if not (1920 <= int(fields["byr"]) <= 2002):
                return False
            if not (2010 <= int(fields["iyr"]) <= 2020):
                return False
            if not (2020 <= int(fields["eyr"]) <= 2030):
                return False
            if not re.match(r"^(59|6\d|7[0-6])in$|^(1[5-8]\d|19[0-3])cm$", fields["hgt"]):
                return False
            if not re.match(r"^#[0-9a-f]{6}$", fields["hcl"]):
                return False
            if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                return False
            if not re.match(r"^\d{9}$", fields["pid"]):
                return False
            return True
        return False

    passports = " ".join(passport_data).split("  ")
    return sum(is_valid(passport) for passport in passports)