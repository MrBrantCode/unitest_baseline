"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, reverses the order of characters in each word, capitalizes all vowels within each reversed word, and returns the modified string. The input string is space-separated and only contains lowercase letters and spaces.
"""

def reverse_string(s):
    words = s.split()
    reversed_words = [word[::-1].capitalize() for word in words]
    return ' '.join(reversed_words)