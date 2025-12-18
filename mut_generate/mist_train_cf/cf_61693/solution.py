"""
QUESTION:
Write a function `reverse_alternate` that takes a string as input, reverses every alternate word in the string while ignoring punctuation and special characters, handles multiple spaces between words, and returns the modified string. The original order of words must be maintained.
"""

import string

def reverse_alternate(sentence):
    # Removes special characters from string and replace multiple whitespace to single
    sentence = ' '.join(''.join(e for e in string if e.isalnum() or e.isspace()) for string in sentence.split())

    words = sentence.split()

    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]

    return ' '.join(words)