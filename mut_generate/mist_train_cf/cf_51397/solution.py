"""
QUESTION:
Write a function `permutations_count` that takes a string `t` as input and returns the number of palindrome permutations possible using the characters in the string. The function should be case-insensitive and consider spaces and punctuation as valid characters. It should return 1 if at least one palindrome permutation is possible and 0 otherwise. The function should handle strings with any combination of letters, spaces, and punctuation.
"""

from collections import Counter
import string

def permutations_count(t):
    # Count characters
    c = Counter(t.lower())

    # Include letters, punctuation and space
    valid_chars = string.ascii_lowercase + string.punctuation + ' '

    # Remove unwanted characters
    c = {k: v for k, v in c.items() if k in valid_chars}

    # Keep track of single characters (for the middle of the palindrome)
    odd_count_chars = [k for k, v in c.items() if v % 2]

    # Check if more than one single character exists
    if len(odd_count_chars) > 1:
        return 0
    else:
        return 1