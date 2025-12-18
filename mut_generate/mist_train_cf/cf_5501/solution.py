"""
QUESTION:
Create a function `reverse_words` that takes a string as input, ignores leading/trailing whitespace, removes punctuation marks/special characters, handles multiple spaces between words, and removes duplicate words. The function should return a string with each word in reverse order.
"""

def reverse_words(string):
    string = string.strip()
    string = ''.join(c for c in string if c.isalnum() or c.isspace())
    words = string.split()
    words = words[::-1]
    words = list(dict.fromkeys(words))
    return ' '.join(words)