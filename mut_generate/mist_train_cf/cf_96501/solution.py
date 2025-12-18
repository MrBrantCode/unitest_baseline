"""
QUESTION:
Write a function called `convert_case` that takes in a string as input and returns a new string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase, without using the built-in `swapcase()` function. The function should preserve the original case of any non-alphabetic characters in the input string.
"""

def convert_case(string):
    converted_string = ''
    for char in string:
        if char.islower():
            converted_string += char.upper()
        elif char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char
    return converted_string