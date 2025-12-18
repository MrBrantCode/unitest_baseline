"""
QUESTION:
Write a function called `is_pangram` that determines if a given string is a pangram, a sentence using every letter of the alphabet at least once. The function should be case-insensitive and assume the input string only contains letters.
"""

def is_pangram(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_string.lower():
            return False
    return True