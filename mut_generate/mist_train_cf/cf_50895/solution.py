"""
QUESTION:
Write a function `find_palindromic_pairs(s)` to find all palindromic pairs of substrings within a given string `s`. The function should ignore punctuation and casing when checking for palindromes. A palindromic pair is defined as a pair of substrings that form a palindrome when concatenated together, disregarding whitespace.
"""

import string
import itertools

def find_palindromic_pairs(s):
    # Remove punctuation and transform to lower case
    s = ''.join(ch for ch in s if ch not in string.punctuation).lower()

    # Split into words
    words = s.split(' ')

    # Get all pairs of words
    pairs = list(itertools.combinations(words, 2))

    # Check if a pair is a palindrome
    palindrome_pairs = [pair for pair in pairs if ''.join(pair) == ''.join(pair)[::-1]]

    return palindrome_pairs