"""
QUESTION:
Write a function `substitute_alphanumeric(text, n, replacement)` that takes a string `text`, an integer `n` between 1 and 26, and a character `replacement`. The function should replace all occurrences of the nth letter in the English alphabet in `text` that are not alphanumeric with `replacement`.
"""

def substitute_alphanumeric(text, n, replacement):
    # retrieve the nth letter in the alphabet
    nth_letter = chr(ord('a') + n - 1)
    
    # substitute all occurrences of the nth letter that are not alphanumeric
    return ''.join([replacement if c == nth_letter and not c.isalnum() else c for c in text])