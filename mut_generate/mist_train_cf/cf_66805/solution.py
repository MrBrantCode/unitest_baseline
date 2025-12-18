"""
QUESTION:
Create a function `roman_to_int` that takes a string `s` representing a Roman numeral as input and returns its numerical representation as an integer. The Roman numeral `s` only contains the characters I, V, X, L, C, D, and M.
"""

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev, total = 0, 0
    for c in s:
        current = roman_dict[c]
        if current > prev:
            total += current - 2 * prev
        else:
            total += current
        prev = current
    return total