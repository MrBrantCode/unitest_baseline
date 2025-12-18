"""
QUESTION:
Create a function `int_to_roman(num)` that converts an integer `num` (1 <= num <= 3999) into its Roman numeral representation, following the standard rules where smaller symbols can be placed before larger symbols to denote subtraction. The function should return a string representing the Roman numeral equivalent of the input integer.
"""

def int_to_roman(num):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    result = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result