"""
QUESTION:
Create a function called `count_unicode_chars` that calculates the frequency of each non-control Unicode character in a given string. The function should take a single string argument `text` and return a dictionary where keys are the unique Unicode characters and values are their frequencies. The function should treat all non-control characters as Unicode characters and should have a time complexity of O(n), where n is the length of the input string.
"""

import unicodedata

def count_unicode_chars(text):
    unicode_chars = {}
    for char in text:
        if unicodedata.category(char)[0] != "C":
            if char in unicode_chars:
                unicode_chars[char] += 1
            else:
                unicode_chars[char] = 1
    return unicode_chars