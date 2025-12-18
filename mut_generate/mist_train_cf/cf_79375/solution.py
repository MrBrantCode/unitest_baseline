"""
QUESTION:
Write a Python function `split_string(s)` that takes a string `s` as input and returns a tuple containing two elements: a list of characters in the string `s` and the count of vowels in the string. The function should be case-insensitive, treating both uppercase and lowercase vowels as the same.
"""

def split_string(s):
    chars = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = sum(1 for char in chars if char.lower() in vowels)
    return chars, vowel_count