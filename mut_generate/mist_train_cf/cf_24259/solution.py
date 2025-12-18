"""
QUESTION:
Create a function named `has_all_alphabet` that determines if a given string contains all 26 letters of the English alphabet, ignoring case. The function should take a single string parameter and return a boolean value indicating whether the string contains all English letters.
"""

def has_all_alphabet(string):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return set(letters).issubset(string.upper())