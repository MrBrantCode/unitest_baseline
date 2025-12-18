"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, removes leading and trailing whitespace, splits the string into words, reverses their order, and returns the resulting string. The function should ignore any leading or trailing whitespace in the input string and separate words by a single space in the output string.
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])