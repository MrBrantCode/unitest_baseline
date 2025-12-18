"""
QUESTION:
Reverse a string of characters and words.

Create a function called 'reverse_string' that takes a string as input, and returns the string with its characters and words reversed.
"""

def reverse_string(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words[::-1])