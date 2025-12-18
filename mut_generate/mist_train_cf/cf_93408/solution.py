"""
QUESTION:
Write a function `split_string` that takes a string as input and returns the string split at the midpoint with the order of the two parts switched. The midpoint is the index of the character closest to the center of the string. If the string length is odd, the character at the midpoint should be included in the first part; if even, it should be included in the second part.
"""

def split_string(s):
    length = len(s)
    midpoint = length // 2

    if length % 2 == 0:
        return s[midpoint:] + s[:midpoint]
    else:
        return s[midpoint + 1:] + s[midpoint] + s[:midpoint]