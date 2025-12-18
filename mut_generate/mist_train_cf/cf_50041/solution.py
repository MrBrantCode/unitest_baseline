"""
QUESTION:
Create a function `remove_vowels` that takes a string `text` as input and returns the string without vowels. The function should be case-insensitive, handling both lowercase and uppercase English vowels, and preserve non-alphabetic characters such as punctuation, special characters, and numbers.
"""

def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])