"""
QUESTION:
Create a function called `int_to_mini_roman` that takes a single integer as input and returns a string. The input integer is guaranteed to be between 1 and 1000, inclusive. The function should convert the input integer to its equivalent in lowercase Roman numerals and return the result as a string.
"""

def int_to_mini_roman(number):
    mapping = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"),
               (100, "c"), (90, "xc"), (50, "l"), (40, "xl"),
               (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    result = ""
    for arabic, roman in mapping:
        while number >= arabic:
            result += roman
            number -= arabic
    return result