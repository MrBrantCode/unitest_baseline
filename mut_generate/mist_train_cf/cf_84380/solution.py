"""
QUESTION:
Write a function `is_five_alpha_chars` that takes a string `appellation` as input and returns a boolean indicating whether it consists of exactly 5 alphabetic characters. The function should return `False` for any non-alphabetic characters or strings of a different length.
"""

def is_five_alpha_chars(appellation):
    # Check if the length of appellation is 5
    if len(appellation) != 5:
        return False
    
    # Check if all characters are alphabetic
    for char in appellation:
        if not char.isalpha():
            return False
    
    # If the length is 5 and all characters are alphabetic
    return True