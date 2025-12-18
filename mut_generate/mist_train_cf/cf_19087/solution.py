"""
QUESTION:
Write a function `int_to_roman(num)` that converts an integer to a Roman numeral string in uppercase. The function should handle integers from 1 to 3999, return "Invalid input" for numbers outside this range, and have a time complexity of O(log n) and space complexity of O(1), where n is the given integer.
"""

def int_to_roman(num):
    if num <= 0 or num >= 4000:
        return "Invalid input"

    roman_nums = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_str = ""
    for value, symbol in roman_nums.items():
        while num >= value:
            roman_str += symbol
            num -= value

    return roman_str