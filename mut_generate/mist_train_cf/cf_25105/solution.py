"""
QUESTION:
Create a function `to_roman` that takes an integer `n` as input and returns its equivalent in Roman numerals. The function should only work with integers from 1 to 3999 and should use the standard Roman numeral mapping.
"""

def to_roman(n):
    roman_mapping = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""
    for number, letter in roman_mapping.items():
        result += letter * (n // number)
        n %= number

    return result