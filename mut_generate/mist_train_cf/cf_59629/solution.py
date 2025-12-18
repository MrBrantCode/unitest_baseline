"""
QUESTION:
Write a function `solve` that takes a string `s` as input. The function should return the string `s` with the following transformations: if `s` contains only alphanumeric characters, swap the case of each alphanumeric character, then sort the characters in descending order and return the result. If `s` contains non-alphanumeric characters, swap the case of each alphanumeric character and return the result without changing the order of the characters. If `s` is an empty string, return it as is.
"""

def solve(s):
    if not s:
        return s
    
    if s.isalnum():
        return ''.join(sorted([c.swapcase() for c in s], reverse=True))
    
    return ''.join(c.swapcase() if c.isalnum() else c for c in s)