"""
QUESTION:
Write a function named `longest_word` that takes a list of alphanumeric strings and returns the length of the longest word, defined as the sequence of characters delimited by whitespace, punctuation, or digits. The function should handle edge cases such as empty input lists, single-character words, and words with diacritical marks or non-Latin characters. Optimize the function for performance by using efficient data structures and algorithms.
"""

import re
def longest_word(words):
    longest = 0
    for word in words:
        # split the word into substrings delimited by whitespace, punctuation, or digits
        substrings = re.split(r'[\s\W\d]+', word)
        # find the length of the longest substring
        for substring in substrings:
            if len(substring) > longest:
                longest = len(substring)
    return longest