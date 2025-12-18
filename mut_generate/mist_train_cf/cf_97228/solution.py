"""
QUESTION:
Create a function named `count_letters` that takes a string as input. The function should return a list of tuples where each tuple contains a unique letter in the string and its corresponding count, ignoring case sensitivity. The list should be sorted in descending order by count, and for letters with the same count, they should be sorted alphabetically. The input string may contain punctuation marks, spaces, and special characters, which should be ignored.
"""

import re
from collections import defaultdict

def count_letters(string):
    # Convert the string to lowercase and remove punctuation marks, spaces, and special characters
    string = re.sub(r'[^a-zA-Z]', '', string.lower())

    # Create a dictionary to store the count of each letter
    letter_counts = defaultdict(int)

    # Iterate over each character in the string
    for char in string:
        # Update the count of the letter in the dictionary
        letter_counts[char] += 1

    # Sort the dictionary by value in descending order
    # If two or more letters have the same count, sort them alphabetically
    sorted_counts = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_counts