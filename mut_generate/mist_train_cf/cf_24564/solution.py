"""
QUESTION:
Create a function `int_to_roman(num)` that takes an integer `num` as input and returns its equivalent Roman numeral representation as a string. The function should handle integers in the range of 1 to 3999 and return a string of Roman numerals. The Roman numeral system uses seven distinct characters: I, V, X, L, C, D, and M, with each character having a specific integer value.
"""

def int_to_roman(num):
    """
    Converts an integer to its equivalent Roman numeral representation.

    Args:
    num (int): The integer to be converted, in the range of 1 to 3999.

    Returns:
    str: The Roman numeral representation of the input integer.

    """
    roman_numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    result = ''
    for n in sorted(roman_numerals.keys(), reverse=True):
        count = num // n
        result += roman_numerals[n] * count
        num %= n
    return result