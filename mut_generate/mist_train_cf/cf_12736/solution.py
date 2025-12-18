"""
QUESTION:
Create a function named `reverse_characters` that takes a string `s` as input and returns a new string where each word's characters are reversed, but the order of the words remains the same.
"""

def reverse_characters(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)