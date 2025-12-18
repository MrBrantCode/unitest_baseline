"""
QUESTION:
Write a function `compare_values` that takes two strings as input and returns the string with the greater sum of ASCII values. If the sums are equal, return the string that comes later alphabetically.
"""

def compare_values(val1, val2):
    ascii_val1 = sum(ord(c) for c in val1)
    ascii_val2 = sum(ord(c) for c in val2)
    if ascii_val1 > ascii_val2:
        return val1
    elif ascii_val1 < ascii_val2:
        return val2
    else:
        if val1 > val2:
            return val1
        else:
            return val2