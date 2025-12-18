"""
QUESTION:
Create a function named `reverse_characters` that takes a string `s` as input, reverses the characters in each word, and returns the resulting string without reversing the order of the words.
"""

def reverse_characters(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)