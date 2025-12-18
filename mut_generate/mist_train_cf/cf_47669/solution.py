"""
QUESTION:
Create a function called `int_to_mini_roman` that converts a positive integer between 1 and 5000 into its lowercase roman numeral representation, ensuring the formation of conducive numeral patterns. The function should return the roman numeral as a string.
"""

def int_to_mini_roman(number):
    # Map of integers to their corresponding roman numerals
    int_to_roman_map = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
                        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
                        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]

    roman_numeral = ''
    for i, numeral in int_to_roman_map:
        while number >= i:
            roman_numeral += numeral
            number -= i
    return roman_numeral