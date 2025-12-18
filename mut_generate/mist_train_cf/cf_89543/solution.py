"""
QUESTION:
Write a function named `swap_case` that takes a string as input, swaps the case of all alphabetic characters, and returns the resulting string. The function should only use a single loop to iterate through the input string and should not use the built-in `swapcase()` function. Non-alphabetic characters in the input string should have their case preserved in the output string.
"""

def swap_case(string):
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result