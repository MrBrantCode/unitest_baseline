"""
QUESTION:
Write a function `solve` that takes a string `s` as input. Swap the case of each alphabetic character in `s` (i.e., convert lowercase to uppercase and vice versa) and leave non-alphabetic characters unchanged. If `s` contains no alphabetic characters, return the reverse of `s`. The function should support Unicode characters beyond the ASCII table.
"""

def solve(s):
    if all(not c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.lower() if c.isupper() else c.upper() for c in s)