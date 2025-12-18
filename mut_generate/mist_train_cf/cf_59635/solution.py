"""
QUESTION:
Write a function `int_to_mini_roman(number)` that converts an integer into its lowercase roman numeral representation as a string. The function should accept integers within the range of -1000 to 1000. If the input is negative, the output should be prepended with a minus sign.
"""

def int_to_mini_roman(number):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]

    if number == 0:
        return "nulla"
    roman_num = ''
    if number < 0:
        roman_num = '-'
        number = -number
    i = 0
    while (number > 0):
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num.lower()