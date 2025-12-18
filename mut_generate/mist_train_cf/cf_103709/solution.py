"""
QUESTION:
Remove all non-alphabet characters from a given string while preserving the original character order.

Create a function called `remove_non_alphabet_chars` that takes a string as input and returns the string after removing all non-alphabet characters. The function should handle any type of non-alphabet characters, including but not limited to punctuation, digits, and whitespace.
"""

def remove_non_alphabet_chars(string):
    alphabet_chars = ''
    for char in string:
        if char.isalpha():
            alphabet_chars += char
    return alphabet_chars