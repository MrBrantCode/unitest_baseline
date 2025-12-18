"""
QUESTION:
Write a function `reverse_non_repeated(s)` that takes a string `s` as input and returns a new string containing all non-repeated characters from `s` in reverse order, excluding spaces and considering uppercase and lowercase letters as distinct characters.
"""

def reverse_non_repeated(s):
    s = s.replace(' ', '')
    unique_chars = [c for c in s if s.count(c) == 1]
    result = ''.join(reversed(unique_chars))
    return result