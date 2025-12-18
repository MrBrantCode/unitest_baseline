"""
QUESTION:
Write a function named `remove_vowels` that takes a string `s` as input and returns the string with all vowels removed. The function should consider both lowercase and uppercase vowels.
"""

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    s = ''.join([char for char in s if char not in vowels])
    return s