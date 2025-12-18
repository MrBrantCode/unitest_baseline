"""
QUESTION:
Create a function `ascii_reverse` that takes a string as input, replaces every character with its corresponding ASCII code, and returns the resulting string in reverse order. The input string only contains letters.
"""

def ascii_reverse(s):
    return ''.join(str(ord(c)) for c in s[::-1])