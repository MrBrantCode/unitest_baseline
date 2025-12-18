"""
QUESTION:
Write a function `is_only_five_alphabets(designation)` that checks if a given string `designation` is exactly 5 characters long and contains only alphabetic characters. The function should return `True` if the string meets these conditions, and `False` otherwise.
"""

def entrance(designation):
    if len(designation) != 5:
        return False
    for character in designation:
        if not character.isalpha():
            return False
    return True