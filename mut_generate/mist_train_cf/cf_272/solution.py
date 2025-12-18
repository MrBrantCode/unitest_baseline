"""
QUESTION:
Write a function `swap_case` that takes a string as input and returns a new string where all lowercase letters are replaced with their corresponding uppercase letters and vice versa. Non-alphabet characters should remain unchanged.
"""

def swap_case(s):
    swapped_string = ""
    for char in s:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char
    return swapped_string