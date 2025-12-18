"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, reverses each word in the string while maintaining their original order, and returns the resulting string.
"""

def reverse_string(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)