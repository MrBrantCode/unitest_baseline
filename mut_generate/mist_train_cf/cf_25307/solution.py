"""
QUESTION:
Write a function named `remove_vowels` that takes a string as input and returns a new string with all vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') removed.
"""

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])