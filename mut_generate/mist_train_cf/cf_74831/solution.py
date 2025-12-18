"""
QUESTION:
Write a function `advanced_roman_to_int` that converts a string of lowercase roman numerals to a positive integer, where the string can be up to 'mm' (2099). The input string will contain roman numerals from 'i' (1) to 'm' (1000) and their combinations. The function should correctly handle subtractive notation, where a smaller numeral appears before a larger one.
"""

def advanced_roman_to_int(roman):
    roman_numerals = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    integer = 0
    i = 0

    while i < len(roman):
        if i+1 < len(roman) and roman_numerals[roman[i]] < roman_numerals[roman[i+1]]:
            integer += roman_numerals[roman[i+1]] - roman_numerals[roman[i]]
            i += 2
        else:
            integer += roman_numerals[roman[i]]
            i += 1
    return integer