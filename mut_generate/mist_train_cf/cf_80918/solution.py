"""
QUESTION:
Implement a function `string_to_int(s: str) -> int` that converts a given string `s` to an integer without using the built-in `int()` function. The function should be able to handle strings containing negative numbers and return the corresponding negative integer value.
"""

def string_to_int(s: str) -> int:
    if s[0] == '-':
        s = s[1:]
        neg = True
    else:
        neg = False
    
    result = 0
    for char in s:
        result = result * 10 + ord(char) - 48  # Use ASCII values to convert strings to integers
    
    if neg:
        result = -result
    
    return result