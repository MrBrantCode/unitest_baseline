"""
QUESTION:
Write a function `swap_case` that takes a string as input and returns a new string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase, preserving the original case of non-alphabetic characters. The function should only use a single loop to iterate through the input string and should not use the built-in `swapcase()` function.
"""

def swap_case(s):
    result = ''
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result