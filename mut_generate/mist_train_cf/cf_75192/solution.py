"""
QUESTION:
Create a function `check_pangram(input_string)` that determines whether the given string is a pangram, meaning it uses every letter of the alphabet at least once. The function should return `True` if the string is a pangram and `False` otherwise. The comparison should be case-insensitive.
"""

def check_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_string.lower():
            return False
    return True