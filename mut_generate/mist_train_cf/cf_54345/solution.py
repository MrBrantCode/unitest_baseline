"""
QUESTION:
Create a function `is_palindromic_consonant(s)` that takes a string `s` as input and returns `True` if the string consists only of consonants and these consonants are in a palindromic pattern, and `False` otherwise. The function should be case sensitive and consider special characters as invalid input. The function should not modify the original string.
"""

def is_palindromic_consonant(s):
    # define consonants
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    filtered_word = ''.join(c for c in s if c in consonants)
    
    # check if word is palindrome
    return filtered_word == filtered_word[::-1]