"""
QUESTION:
Given a string, write a function `longest_word_length` that finds the length of the longest word that can be formed by rearranging the characters of the string. The function should ignore whitespace characters and special characters, and return the length of the longest word (not the word itself). The time complexity of the solution should be O(n log n), where n is the length of the string.
"""

import re

def longest_word_length(string):
    # Remove whitespace and special characters
    modified_string = re.sub(r'[^a-zA-Z]', '', string)

    # Convert modified string to a list of characters
    chars = list(modified_string)

    # Sort the list of characters
    chars.sort()

    current_length = 0
    max_length = 0

    for i in range(len(chars)):
        if i > 0 and chars[i] == chars[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)

    return max_length