"""
QUESTION:
Implement a function called `is_uppercase_letter` that takes a single character as input and returns `True` if the character is an uppercase letter (A-Z) and `False` otherwise. The function should not use any built-in functions or libraries and must have a time complexity of O(1).
"""

def is_uppercase_letter(char):
    if len(char) != 1:
        return False

    ascii_value = ord(char)
    return 65 <= ascii_value <= 90