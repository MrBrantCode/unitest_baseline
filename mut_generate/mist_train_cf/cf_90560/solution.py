"""
QUESTION:
Write a function `reverse_words` that takes a string containing only alphabetic characters and spaces as input, reverses the characters within each word while maintaining the word order, and returns the resulting string. The function should ignore any leading or trailing spaces and handle multiple consecutive spaces between words.
"""

def reverse_words(string):
    string = string.strip()
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string