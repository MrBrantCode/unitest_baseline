"""
QUESTION:
Write a function called `reverse_words` that takes a string `s` as input and returns the string with the words separated by spaces in reverse order. The function should handle multiple spaces between words and leading/trailing spaces.
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])