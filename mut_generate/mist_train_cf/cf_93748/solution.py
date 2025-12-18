"""
QUESTION:
Write a function named `reverse_words` that takes a string as input, reverses the order of the words while maintaining each word's original order, removes leading and trailing spaces, and collapses multiple consecutive spaces into a single space, and returns the resulting string.
"""

def reverse_words(string):
    words = string.split(' ')
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words).strip()
    reversed_string = ' '.join(reversed_string.split())
    return reversed_string