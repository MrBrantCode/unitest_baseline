"""
QUESTION:
Create a function `count_upper_vowels(s)` that takes a string `s` as input and returns the count of uppercase vowels present at even indices in the string. The function should only consider the characters 'A', 'E', 'I', 'O', and 'U' as vowels.
"""

def entance(s):
    """
    This function counts the number of capital letters which are vowels on even indices in the string.
    """
    upper_vowels = 'AEIOU'
    even_letters = s[::2]
    counter = sum(1 for letter in even_letters if letter in upper_vowels)
    return counter