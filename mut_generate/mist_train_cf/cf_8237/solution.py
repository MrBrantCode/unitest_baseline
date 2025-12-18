"""
QUESTION:
Write a function `string_to_float` that takes a string representing a valid positive decimal number with up to 5 decimal places and returns its float representation. The function should handle leading and trailing whitespace in the string, and should not use any built-in conversion functions or libraries.
"""

def string_to_float(s):
    s = s.strip()
    result = 0
    decimal_found = False
    decimal_places = 0
    for c in s:
        if c.isdigit():
            result = result * 10 + (ord(c) - ord('0'))
            if decimal_found:
                decimal_places += 1
        elif c == '.':
            decimal_found = True
    if decimal_found:
        result /= 10 ** decimal_places
    return result