"""
QUESTION:
Write a function named `split_string` that takes a string `s` as input and returns a tuple containing three values: a list of characters in the string, the count of vowels in the string, and the count of consonants in the string. The function should be case-insensitive and should handle special characters and numbers in the string.
"""

def split_string(s):
    chars = list(s.lower())
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for char in chars:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return chars, vowel_count, consonant_count