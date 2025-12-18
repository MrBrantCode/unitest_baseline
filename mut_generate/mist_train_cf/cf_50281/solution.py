"""
QUESTION:
Design a function `advanced_roman_to_int` to convert a complex string of lowercase roman numerals to equivalent positive integers. The input roman numeral string should be between 'i' and 'cdxxvi'.
"""

def advanced_roman_to_int(roman):
    roman_dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    integer = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            integer += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
        else:
            integer += roman_dict[roman[i]]
    return integer