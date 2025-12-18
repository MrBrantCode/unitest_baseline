"""
QUESTION:
Create a function called `longest_word` that takes a list of strings as input. The function should return the longest word in the list, considering only words that consist entirely of lowercase alphabetic characters and excluding any words that contain special characters or digits.
"""

import re

def longest_word(words):
    longest = ""
    for word in words:
        if not re.search(r'[^a-z]', word) and len(word) > len(longest):
            longest = word
    return longest