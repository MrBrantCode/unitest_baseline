"""
QUESTION:
Write a function `reverse_string` that takes a string as input, removes any punctuation marks, converts it to lowercase, and reverses the order of the words. The function should return the modified string.
"""

import string

def reverse_string(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.lower()
    words = s.split()
    words.reverse()
    return ' '.join(words)