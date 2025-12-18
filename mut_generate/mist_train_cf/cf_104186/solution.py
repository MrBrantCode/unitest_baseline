"""
QUESTION:
Write a function `check_string(s)` that takes a string `s` as input and returns `True` if it consists only of lowercase alphabetic characters and contains at least one vowel, and `False` otherwise.
"""

def check_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    has_vowel = False

    # Check if all characters are lowercase alphabetic
    if s.islower():
        # Check if the string contains at least one vowel
        for char in s:
            if char in vowels:
                has_vowel = True
                break

    return s.islower() and has_vowel