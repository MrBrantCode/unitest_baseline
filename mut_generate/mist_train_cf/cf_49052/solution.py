"""
QUESTION:
Create a function `is_pangram` that accepts an array of characters as input and returns a boolean indicating whether the input array contains all 26 letters of the alphabet, disregarding case.
"""

def is_pangram(input_chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_chars.lower():
            return False
    return True