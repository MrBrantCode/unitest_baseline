"""
QUESTION:
Write a function named `int_to_mini_roman` that takes an integer `num` between 1 and 1000 as input and returns its lowercase Roman numeral string representation. The function should ensure that the correct Roman numeral patterns are formed in the output.
"""

def int_to_mini_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']

    mini_roman = ''
    for i in range(len(values)):
        count = num // values[i]
        num %= values[i]

        mini_roman += numerals[i] * count

    return mini_roman