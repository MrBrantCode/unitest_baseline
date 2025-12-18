"""
QUESTION:
Write a function `longest_word_length` that takes a string as input, and returns the length of the longest word that can be formed by rearranging the characters of the string. The function should ignore whitespace characters and special characters, and return the length of the longest word, not the actual word itself. The time complexity of the solution should be O(n log n), where n is the length of the string.
"""

import re

def longest_word_length(s):
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    s = sorted(s)

    max_length = current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)