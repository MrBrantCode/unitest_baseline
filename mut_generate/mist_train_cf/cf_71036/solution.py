"""
QUESTION:
Create a function `check_pangram(input_str)` that determines whether a given alphanumeric string contains every letter of the alphabet at least once, disregarding case. The function should return a boolean value indicating whether the input string is a pangram.
"""

def check_pangram(input_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_str.lower():
            return False
    return True