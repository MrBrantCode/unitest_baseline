"""
QUESTION:
Create a function named `is_vowel` that takes a single-character string as input. The function should return `True` if the input character is a vowel (either uppercase or lowercase) and `False` otherwise.
"""

def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char.lower() in vowels:
        return True
    return False