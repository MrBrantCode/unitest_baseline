"""
QUESTION:
Create a function named `count_letters` that takes a string as input and returns a list of tuples. The list should contain the count of each unique letter in the string, ignoring case sensitivity, in descending order. If two or more letters have the same count, they should be sorted alphabetically. The string may contain punctuation marks, spaces, and special characters.
"""

import re
from collections import defaultdict

def count_letters(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    letter_counts = defaultdict(int)

    for char in string:
        letter_counts[char] += 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_counts