"""
QUESTION:
Write a function `intToRoman(num)` that converts an integer `num` to a roman numeral. The function should take an integer as input and return a string representing the roman numeral equivalent of the input integer.

The input integer `num` is in the range `[1, 3999]` and is guaranteed to be a valid integer. The roman numeral representation should follow the standard rules of roman numerals, where the symbols are represented from largest to smallest from left to right, and the subtraction rules are applied for numbers like 4, 9, 40, 90, 400, and 900.
"""

def intToRoman(num):
    value = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbol = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // value[i]):
            roman += symbol[i]
            num -= value[i]
        i += 1
    return roman