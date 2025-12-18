"""
QUESTION:
Implement a function `to_int` that takes a string of numeric characters as input and returns the corresponding positive integer value. The input string will only contain digits (0-9) and will not be empty. Do not use any built-in conversion functions or libraries.
"""

def to_int(s):
    result = 0
    for char in s:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result