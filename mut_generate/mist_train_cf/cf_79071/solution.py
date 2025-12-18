"""
QUESTION:
Write a function `cumulative_character_count` that calculates the cumulative count of alphanumeric characters within an array of distinct textual elements. The function should be case sensitive and exclude punctuation, whitespace, and special non-alphabetical characters.
"""

import string

def cumulative_character_count(arr):
    count = 0
    for text in arr:
        for char in text:
            if char.isalnum():  
                count += 1

    return count