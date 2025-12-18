"""
QUESTION:
Write a function named `check_pangram` that takes an input string and returns `True` if it contains all 26 alphabetic characters (from 'a' to 'z') at least once, and `False` otherwise. The function should be case-insensitive.
"""

def is_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_string.lower():
            return False

    return True