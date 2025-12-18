"""
QUESTION:
Create a function `to_roman(num: int) -> str` that takes an integer `num` (1 <= num <= 3999) as input and returns its Roman numeral representation as a string. The Roman numeral representation should follow the standard rules of Roman numerals, including subtractive notation.
"""

def to_roman(num: int) -> str:
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    values = sorted(roman_numerals.keys(), reverse=True)
    result = ''
    i = 0
    while num > 0:
        div = num // values[i]
        num %= values[i]
        result += roman_numerals[values[i]] * div
        i += 1
    return result