"""
QUESTION:
Given a string `s` of lowercase English letters, write a function `longest_palindrome_length(s: str) -> int` to determine the length of the longest palindrome that can be constructed using the letters in `s`. The function should return an integer representing the maximum length.
"""

import collections

def longest_palindrome_length(s: str) -> int:
    frequencies = collections.Counter(s)
    length = 0
    odd_letters = 0

    for letter in frequencies:
        count = frequencies[letter]
        length += count
        if count % 2 == 1:
            odd_letters += 1

    if odd_letters > 0:
        length -= (odd_letters - 1)

    return length