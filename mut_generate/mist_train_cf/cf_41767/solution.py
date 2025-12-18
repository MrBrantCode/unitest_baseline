"""
QUESTION:
Implement a function `is_subnational1` that takes a string `location_code` as input and returns a boolean indicating whether it is a subnational level 1 code. The function should return `True` if the `location_code` meets the following conditions and `False` otherwise:
- It consists of a single uppercase letter followed by exactly 6 digits.
- The letter is the country code and can be any uppercase letter from A to Z.
- The first digit of the region code (the 6 digits) is not "0" when the country code is "L".
"""

def is_subnational1(location_code):
    if len(location_code) != 7:
        return False  

    country_code = location_code[0]
    region_code = location_code[1:]

    if not (country_code.isalpha() and country_code.isupper()):
        return False  

    if not region_code.isdigit() or len(region_code) != 6:
        return False  

    return country_code == "L" and region_code[0] != "0"